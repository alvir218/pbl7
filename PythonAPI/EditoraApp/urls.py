from django.conf.urls import url, urls
from django.urls.conf import path
from EditoraApp import views

urlpatterns = [
    path('editora', views.EditoraApi),
    path('editora/<int:id>', views.EditoraApi),
]
