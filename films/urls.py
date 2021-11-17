from django.urls import path
from .views import (
    FilmCreateView,
    FilmDeleteView,
    FilmDetailView,
    FilmListView,
    FilmUpdateView,
)

urlpatterns = [
    path("", FilmListView.as_view(), name="film_list"),
    path("<int:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path("create/", FilmCreateView.as_view(), name="film_create"),
    path("<int:pk>/update/", FilmUpdateView.as_view(), name="film_update"),
    path("<int:pk>/delete/", FilmDeleteView.as_view(), name="film_delete"),
]