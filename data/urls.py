from django.urls import path

from . views import HomeView, LikeView, CategoryListView, CategoryView, DeletePostView, AddCategoryView, PostDetailView, AddPostView, UpdatePostView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    path("post/edit/<int:pk>/", UpdatePostView.as_view(), name="update_post"),
    path("post/<int:pk>/delete/", DeletePostView.as_view(), name="delete_post"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_details"),
    path("category/<str:cats>/", CategoryView, name="category"),
    path("category-list/", CategoryListView, name="category-list"),
    path("like_post/<int:pk>/", LikeView, name="like_post"),
]
