from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import UserProfileChangeForm, UserProfileCreationForm
from .models import UserProfile
from apps.post.models import Post


class RegisterView(CreateView):

    model = UserProfile
    form_class = UserProfileCreationForm
    template_name = 'user/profile/register.html'
    success_url = reverse_lazy('user_login')


class CustomLoginView(LoginView):

    template_name = 'user/profile/login.html'
    success_url = reverse_lazy('home')


class UserProfileUpdateView(UpdateView):
    
    model = UserProfile
    form_class = UserProfileChangeForm
    template_name = 'user/profile/update.html'
    slug_field = 'username' # the name of field on the model
    slug_url_kwarg = 'username' # the name of url keyword

    def get_success_url(self, **kwargs):
        return reverse('user_profile', kwargs={'username': self.get_object().username})


class UserProfileDetailView(DetailView):
    
    model = UserProfile
    template_name = 'user/profile/profile.html'
    slug_field = 'username' # the name of slug field on model (also is looking up field)
    slug_url_kwarg = 'username' # the name of kwargs in url
    field = '__all__'

    # def get_object(self):
    #     return UserProfile.objects.get(username=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, *arg, **kwargs):
        context = super().get_context_data(*arg, **kwargs)

        # filter all posts related to this user (my post, like)
        # at current, only my post
        posts = Post.objects.filter(author=self.get_object())
        context['posts'] = posts

        return context


# Change Password
class UserProfilePasswordChangeView(PasswordChangeView):

    template_name = 'user/password/change.html'
    success_url = reverse_lazy('password_change_complete')


class UserProfilePasswordChangeDoneView(PasswordChangeDoneView):

    template_name = 'user/password/change_complete.html'


# Reset Password
class UserProfilePasswordResetView(PasswordResetView):

    template_name = 'user/password/reset.html'
    email_template_name = 'user/password/reset_email.html'
    subject_template_name = 'user/password/reset_subject.txt'
        

class UserProfilePasswordResetDoneView(PasswordResetDoneView):

    template_name = 'user/password/reset_done.html'


class UserProfilePasswordResetConfirmView(PasswordResetConfirmView):

    template_name = 'user/password/reset_confirm.html'
    success_url = reverse_lazy('_password_reset_complete')


class UserProfilePasswordResetCompleteView(PasswordResetCompleteView):

    template_name = 'user/password/reset_complete.html'


