from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  #admin-ka
    path('', include('main.urls')), # отпровляю запрос в main/urls.py
    path('posts/', include('posts.urls')),   # отпровляю запрос в posts/urls.py
]
