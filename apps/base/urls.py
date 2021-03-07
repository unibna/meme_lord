from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.SearchView.as_view(), name='search'),
    path('home/',  views.HomeView.as_view(), name='home')
]