from django.urls import path

from cinema.views import movie_list, movie_detail, genre_list, genre_detail

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre_detail"),
]

app_name = "cinema"
