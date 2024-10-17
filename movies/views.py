from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from datetime import datetime, timedelta
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request): # Pagina principal
    return render(request, 'home.html')

@login_required
def account(request):
    return render(request, 'login/account.html')

@login_required
def movies_rented(request):
    try:
        # Obtener el socio actual
        socio = Socio.objects.get(user=request.user)
        
        # Obtener los alquileres del socio
        alquileres = Alquiler.objects.filter(id_socio=socio, as_delivered__isnull=True)  # Solo alquileres no entregados
        
        # Obtener los IDs de los ejemplares alquilados
        ejemplares_alquilados_ids = alquileres.values_list('id_ejemplar', flat=True)
        
        # Obtener las películas asociadas a esos ejemplares
        peliculas_alquiladas = Pelicula.objects.filter(ejemplar__id__in=ejemplares_alquilados_ids).distinct()

        return render(request, 'movies/rented_movies.html', {
            'peliculas_alquiladas': peliculas_alquiladas
        })
        
    except Socio.DoesNotExist:
        return render(request, 'movies/rented_movies.html', {'error': 'Debes registrarte como socio para ver tus películas alquiladas.'})

@login_required
def movies(request): # Muestra la lista de peliculas
    movies = Pelicula.objects.all()
    return render(request, 'movies/movies.html', {
        'movies': movies
    })

@login_required
def add_consigner(request):
    try:
        socio = Socio.objects.get(user=request.user)
    except Socio.DoesNotExist:
        return render(request, 'socios/add_consigner.html', {'error': 'Debes registrarte como socio primero.'})

    if Codeudor.objects.filter(id_socio=socio).exists():
        return render(request, 'socios/add_consigner.html', {'message': 'Ya tienes un codeudor asignado.'})

    if request.method == 'POST':
        codeudor_form = CodeudorForm(request.POST, socio=socio)
        if codeudor_form.is_valid():
            codeudor = codeudor_form.save(commit=False)
            codeudor.id_socio = socio  # Asigna el socio actual al codeudor
            codeudor.save()
            return redirect('movies')  # Redirige a donde quieras después de agregar el codeudor
    else:
        codeudor_form = CodeudorForm(socio=socio)

    return render(request, 'socios/add_consigner.html', {
        'codeudor_form': codeudor_form
    })

@login_required
def register_partner(request):
    try:
        socio = Socio.objects.get(user=request.user)
        is_partner = True 
    except Socio.DoesNotExist:
        socio = None
        is_partner = False  

    if request.method == 'POST' and not is_partner:
        socio_form = SocioForm(request.POST)
        if socio_form.is_valid():
            socio = socio_form.save(commit=False)
            socio.user = request.user  # Asociar el socio al usuario autenticado
            socio.save()
            return redirect('movies')
    else:
        socio_form = SocioForm()

    return render(request, 'socios/socio.html', {
        'socio_form': socio_form,
        'is_partner': is_partner, 
    })

@login_required
def rent_movie(request, movie_id):
    # Verificar si el usuario está registrado como socio
    try:
        socio = Socio.objects.get(user=request.user)
        movie = Pelicula.objects.get(id=movie_id)
    except Socio.DoesNotExist:
        return render(request, 'movies/rent_movie.html', {'error_socio': 'You must register as a partner to rent a movie.'})
    except Pelicula.DoesNotExist:
        return render(request, 'movies/rent_movie.html', {'error_pelicula': 'Movie not found.'})

    # Verificar si el socio tiene un codeudor
    codeudor_exists = Codeudor.objects.filter(id_socio=socio).exists()

    ejemplar_disponible = Ejemplar.objects.filter(id_pelicula=movie).exclude(
    id__in=Alquiler.objects.filter(as_delivered__isnull=True).values_list('id_ejemplar', flat=True)).first()

    if not ejemplar_disponible:
        return render(request, 'movies/rent_movie.html', {'error_disponibilidad': 'There are no copies available for rent.'})

    if request.method == 'POST':
        alquiler_form = AlquilerForm(request.POST)

        if 'confirm' in request.POST:
            if alquiler_form.is_valid():
                # Verificar que el ejemplar aún esté disponible
                if ejemplar_disponible and ejemplar_disponible not in Alquiler.objects.filter(as_delivered=False).values_list('id_ejemplar', flat=True):
                    alquiler = alquiler_form.save(commit=False)
                    alquiler.id_socio = socio
                    alquiler.id_ejemplar = ejemplar_disponible

                    # Asignar fechas de alquiler y devolución
                    alquiler.fecha_alquiler = datetime.now().strftime('%Y-%m-%d')
                    alquiler.fecha_devolucion = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
                    alquiler.save()

                    return redirect('movies')  # Redirige a la lista de películas después de confirmar
                else:
                    return render(request, 'movies/rent_movie.html', {'error_disponibilidad': 'Este ejemplar ya está alquilado, elige otro.'})

        else:
            # Mostrar la información del alquiler antes de confirmar
            if alquiler_form.is_valid():
                alquiler_preview = {
                    'socio': socio,
                    'ejemplar': ejemplar_disponible,
                    'fecha_alquiler': datetime.now().strftime('%Y-%m-%d'),
                    'fecha_devolucion': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
                }

                return render(request, 'movies/rent_movie.html', {
                    'alquiler_preview': alquiler_preview,
                    'alquiler_form': alquiler_form,
                    'codeudor_exists': codeudor_exists,
                    'movie': movie,
                    'confirm': True  # Indicamos que se está en la pantalla de confirmación
                })

    else:
        # Crear el formulario con la fecha de alquiler y devolución
        alquiler_form = AlquilerForm(initial={
            'fecha_alquiler': datetime.now().strftime('%Y-%m-%d'),
            'fecha_devolucion': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
        })

    return render(request, 'movies/rent_movie.html', {
        'alquiler_form': alquiler_form,
        'socio': socio,
        'codeudor_exists': codeudor_exists,
        'ejemplar_disponible': ejemplar_disponible
    })

@login_required
def movie_details(request, movie_id):
    movie = get_object_or_404(Pelicula, pk=movie_id)
    movies = Reparto.objects.select_related('id_pelicula', 'id_actores').filter(id_pelicula=movie.id)
    director = Pelicula.objects.select_related('id_director').filter(id=movie.id).first()
    return render(request, 'movies/movie_details.html', {'movies': movies, 'movie': movie, 'director': director})

@login_required
def movie_update(request, movie_id): # Mostrar y actualizar datos de las peliculas
    if request.method == 'GET':
        movie = get_object_or_404(Pelicula, pk=movie_id)
        form = MovieForm(instance=movie)
        return render(request, 'movies/movie_update.html', {'movie': movie, 'form': form})
    else:
        try:
            movie = get_object_or_404(Pelicula, pk=movie_id)
            form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies')
        except ValueError:
            return render(request, 'movies/movie_update.html', {'movie': movie, 'form': form, 'error': 'Error updating movie!'})

@login_required
def delete_movie(request, movie_id): # Borrar pelicula
    movie = get_object_or_404(Pelicula, pk=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies')

@login_required
def add_movie(request): # Funcion add_movie (agregar pelicula)
    if request.method == 'GET':
        return render(request, 'movies/add_movie.html', {
            'form': MovieForm
        })
    else:
        try:
            form = MovieForm(request.POST, request.FILES)
            new_movie = form.save(commit=False)
            new_movie.user = request.user
            form.save()
            return redirect('movies')
        except ValueError:
            return render(request, 'movies/add_movie.html', {
            'form': MovieForm,
            'error': 'Porfavor ingresa datos validos!'
        })

@login_required
def search_movie(request): # Funcion para buscar la pelicula (por director, actor y titulo)
    query = request.GET.get('query') 
    if query:
        movies = Pelicula.objects.filter(titulo__icontains=query)
        actores = Reparto.objects.select_related('id_actores', 'id_pelicula').filter(id_actores__nombre__icontains=query)
        directores = Pelicula.objects.select_related('id_director').filter(id_director__nombre__icontains=query)
        if movies:
            return render(request, 'movies/search_movies.html', {'movies': movies, 'query': query})
        elif actores:
            return render(request, 'movies/search_movies.html', {'actores': actores, 'query': query})
        elif directores:
            return render(request, 'movies/search_movies.html', {'directores': directores, 'query': query})
    else:
        movies = Pelicula.objects.all() 
    return render(request, 'movies/search_movies.html', {'movies': movies, 'query': query})

@login_required
def exit(request): # Funcion logout (cerrar sesion)
    logout(request)
    return redirect('home')

def signup(request): # Funcion signup (registrar usuario)
    if request.method == 'GET':
        return render(request, 'login/signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('movies')
            except:
                return render(request, 'login/signup.html', {
                'form': UserCreationForm,
                'error': 'User alredy exists'
        })
    return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Password do not match'
        })

def entry(request): # Funcion Login (Iniciar sesion)
    if request.method == 'GET':
        return render(request, 'login/login.html', {
            'form': AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login/login.html', {
            'form': AuthenticationForm,
            'error': 'Username or password is incorrect'
    })
        else:
            login(request, user)
            return redirect('movies')