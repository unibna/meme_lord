from django.db import models
from apps.user.models import UserProfile
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse, reverse_lazy

# Create your models here.
class Category(models.Model):
    # id field created in defautl
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def __generate_unique_slug(self):

        unique_slug = slugify(self.name)
        counter = 1
        
        # check if slug exists
        checking_slug = unique_slug
        while Category.objects.filter(slug=checking_slug).exists():
            checking_slug = f"{unique_slug}-{counter}"
            counter += 1

        return checking_slug

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = self.__generate_unique_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        
        if not self.slug:
            self.slug = self.__generate_unique_slug()
        
        return reverse('category_detail', kwargs={'slug': self.slug})
    

class Post(models.Model):
    # id field created in defautl
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, null=True)
    meme = models.ImageField(upload_to='meme/')
    description = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    def __generate_unique_slug(self):

        unique_slug = slugify(self.title)
        counter = 1
        
        # check if slug exists
        checking_slug = unique_slug
        while Category.objects.filter(slug=checking_slug).exists():
            checking_slug = f"{unique_slug}-{counter}"
            counter += 1

        return checking_slug

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = self.__generate_unique_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        
        if not self.slug:
            self.slug = self.__generate_unique_slug()
        
        return reverse('post_detail', kwargs={'slug': self.slug})

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()


class Comment(models.Model):
    # id field created in defautl
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=150, default="Anonymous", blank=True)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)


