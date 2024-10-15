from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('movies/', views.movies, name='movies'),
    path('logout/', views.exit, name='logout'),
    path('login/', views.entry, name='login'),
    path('movies/add/', views.add_movie, name='add_movie'),
    path('movies/edit/<int:movie_id>/', views.movie_update, name='movie_update'),
    path('movies/view/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('movies/<int:movie_id>/delete/', views.delete_movie, name='delete_movie'),
    path('movies/search/', views.search_movie, name='search_movies'),
    path('movies/rent/<int:movie_id>', views.rent_movie, name='rent_movie'),
    path('register/partner/', views.register_partner, name='partner_register'),
    path('account/', views.account, name='account'),
    path('account/rented/movies/', views.movies_rented, name='rented_movies'),
    path('account/add/consigner/', views.add_consigner, name='add_consigner')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)