from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

DEFAULT_AVATAR = 'avatar/default.png'

# Create your models here.
class UserProfile(AbstractUser):   
    avatar = models.ImageField(upload_to='avatar/', default=DEFAULT_AVATAR)
    
    def __str__(self):
        
        return self.username

    def get_profile_url(self):
        # combine 'user_profile' url to username field (aka a slug in this case)
        
        return reverse('user_profile', kwargs={'username': self.username})

    def get_update_url(self):
        # combine 'user_profile' url to username field (aka a slug in this case)

        return reverse('user_update', kwargs={'username': self.username})
