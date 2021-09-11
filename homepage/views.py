from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
from .models import Photo


class IndexView(generic.ListView):
    template_name = 'homepage/index.html'
    context_object_name = 'all_photos'

    def get_queryset(self):
        return Photo.objects.all()


class DetailedView(generic.DetailView):
    model = Photo
    template_name = 'homepage/detailed.html'
