from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('some_uri/', views.index_t, name='index'),
]
