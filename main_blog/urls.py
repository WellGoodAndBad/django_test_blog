from django.urls import path
from .views import HomePageView, PostView, NewPost, DeletePost, EditPost, AddComment


app_name = "main_blog"

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('tag/<slug>/', HomePageView.as_view(), name='posts_by_tag'),
    path('new_post/', NewPost.as_view(), name='add_post'),
    path('delete/<slug:slug>/', DeletePost.as_view(), name='del_post'),
    path('edit/<slug:slug>/', EditPost.as_view(), name='edit_post'),
    path('new_comment/<int:pk>/', AddComment.as_view(), name='new_comment'),
    path('<slug:slug>/', PostView.as_view(), name='post_page'),
]