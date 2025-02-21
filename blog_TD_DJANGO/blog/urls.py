from django.urls import path
from .views import post_list, post_detail, create_post, index, blog

urlpatterns = [
    path('', index, name='index'),  # Page d'accueil
    path('blog/', blog, name='blog'),  # Page du blog
    path('post/<int:post_id>/', post_detail, name='post_detail'),  # Détail d'un post
    path('create/', create_post, name='create_post'),  # Création d'un post
]
