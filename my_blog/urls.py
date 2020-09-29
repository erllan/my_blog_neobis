from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('addBlog/', views.addBlog, name='addBlog'),
    path('blog/<int:id>', views.blog, name='blog'),
    path('comment/<int:id_blog>', views.comment , name='comment')
]
