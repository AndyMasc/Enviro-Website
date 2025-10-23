from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('what_is_it/', views.what_is_it, name='what_is_it'),
    path('issue/', views.issue, name='issue'),
    path('solutions/', views.solutions, name='solutions'),
]