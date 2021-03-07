from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreationView.as_view(), name='category_create'),
    # url(r'^category/(?P<slug>)/$', views.CategoryDetailView.as_view(), name="category_detail"),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),

    path('post/', views.PostListView.as_view(), name='post_list'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name="post_detail"),
    url(r'^post/update/(?P<slug>[-\w]+)/$', views.PostUpdateView.as_view(), name="post_update"),
    url(r'^post/delete/(?P<slug>[-\w]+)/$', views.PostDeleteView.as_view(), name="post_delete"), 
    # path('search', views.SearchingView.as_view(), name='search'),
]