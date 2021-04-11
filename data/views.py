from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from . models import Post, Category, Comment
from . forms import PostForm, EditPostForm, CategoryForm, AddCommentForm
from django.urls import reverse_lazy, reverse
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "data/home.html"
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "data/post_details.html"

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        
        likes_stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = likes_stuff.total_likes()   

        liked = False
        if likes_stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes 
        context['liked'] = liked 
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, "data/category_list.html", {"cat_menu_list": cat_menu_list})

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "data/add_post.html"


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = "data/comment.html"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')


  
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'data/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'data/delete_post.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "data/add_category.html"


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, "data/categories.html",{"cats": cats.title().replace('-', ' '), "category_posts": category_posts})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_details', args=[str(pk)]))

