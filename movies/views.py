from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie

class MovieListView(ListView):
    template_name = "movies/movie_list.html"
    model = Movie

class MovieDetailView(DetailView):
    template_name = "movies/movie_detail.html"
    model = Movie

class MovieUpdateView(UpdateView):
    template_name = "movies/movie_update.html"
    model = Movie
    fields = ["title", "description", "user", "rating"]


class MovieCreateView(CreateView):
    template_name = "movies/movie_create.html"
    model = Movie
    fields = ["title", "description", "user", "rating"]


class MovieDeleteView(DeleteView):
    template_name = "movies/movie_delete.html"
    model = Movie
    success_url = reverse_lazy("movie_list")