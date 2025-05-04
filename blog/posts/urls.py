from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index, name='index'),  #главная список новостей /posts
    path('new_post/', views.new_post), # форма добовления поста /posts/new_post
    path('10/', views.page_10),  # страница пустая /posts/10
    path('create_post/', views.create_post) # метод POST который принемает данные из формы /posts/create_post

]