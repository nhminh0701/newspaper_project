#from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models

# Create your views here.
class ArticleCreateView(CreateView):
    model = models.Articles
    template_name = 'article_new.html'
    fields = ['title', 'body',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleListView(ListView):
    model = models.Articles
    template_name = 'article_list.html'

class ArticleDetailView(DetailView): 
    model = models.Articles 
    template_name = 'article_detail.html'


class ArticleUpdateView(UpdateView):
    model = models.Articles
    fields = ['title', 'body',]
    template_name = 'article_edit.html'
    
class ArticleDeleteView(DeleteView):
    model = models.Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
