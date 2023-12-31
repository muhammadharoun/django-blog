from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        '-published_date')
    # queryset = Post.objects.all()

    template_name = 'blogging/list.html'


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = 'blogging/detail.html'

