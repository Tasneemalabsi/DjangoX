from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Film

class FilmListView(ListView):
    template_name = "films/film_list.html"
    model = Film

class FilmDetailView(DetailView):
    template_name = "films/film_detail.html"
    model = Film

class FilmUpdateView(UpdateView):
    template_name = "films/film_update.html"
    model = Film
    fields = ["title", "description", "user", "rating"]


class FilmCreateView(CreateView):
    template_name = "films/film_create.html"
    model = Film
    fields = ["title", "description", "user", "rating"]


class FilmDeleteView(DeleteView):
    template_name = "films/film_delete.html"
    model = Film
    success_url = reverse_lazy("film_list")