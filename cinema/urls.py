from django.urls import path

from cinema.views import movie_list, movie_detail, genre_list, genre_detail, ActorDetail, ActorList, CinemaHallViewSet

cinema_hall_list = CinemaHallViewSet.as_view(actions={"get": "list", "post": "create"})
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"})

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre_detail"),
    path("actors/", ActorList.as_view(), name="genre-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor_detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema_hall_list"),
    path("cinema_halls/<int:pk>/", cinema_hall_detail, name="cinema_hall_detail"),
]

app_name = "cinema"
