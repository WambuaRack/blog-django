from django.urls import path
from .views import blog_list, create_blog  # Import views

urlpatterns = [
    path('blogs/', blog_list, name='blog-list'),  # Handles GET (Fetching all blogs)
    path('blogs/create/', create_blog, name='create-blog'),  # Handles POST (Creating a blog)
]
