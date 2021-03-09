from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='user_login'),
    path('register/', views.RegisterView.as_view(), name='user_register'),
    url(r'^profile/(?P<username>[-\w]+)/$', views.UserProfileDetailView.as_view(), name="user_profile"),
    url(r'^update/(?P<username>[-\w]+)/$', views.UserProfileUpdateView.as_view(), name="user_update"),
    url(r'^password_change/$', views.UserProfilePasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change_done/$', views.UserProfilePasswordChangeDoneView.as_view(), name='password_change_complete'),

    path('password_reset/', views.UserProfilePasswordResetView.as_view(), name='password_reset'),
    
    path('password_reset/done/', views.UserProfilePasswordResetDoneView.as_view(), name='password_reset_done'),

    path('password_reset/confirm/<uidb64>/<token>', views.UserProfilePasswordResetConfirmView.as_view(), name ='_password_reset_confirm'),

    path('password_reset/complete/', views.UserProfilePasswordResetCompleteView.as_view(), name ='_password_reset_complete'),

]