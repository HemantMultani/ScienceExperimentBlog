from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:name>', views.post, name='post')
]
