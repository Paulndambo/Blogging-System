from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from . models import Post, Category
from . forms import PostForm, EditPostForm, CategoryForm
from django.urls import reverse_lazy
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "data/home.html"
    ordering = ['-post_date']

class PostDetailView(DetailView):
    model = Post
    template_name = "data/post_details.html"

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "data/add_post.html"

class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "data/add_category.html"
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'data/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'data/delete_post.html'
    success_url = reverse_lazy('home')
"""
def home(request):
    return render(request, "data/home.html", {})
"""
