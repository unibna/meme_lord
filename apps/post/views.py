from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView

from .models import *
from . import forms

from itertools import chain


class CategoryCreationView(CreateView):

    model = Category
    fields = '__all__'
    template_name = 'post/category/create.html'


class CategoryListView(ListView):

    model = Category
    template_name = 'post/category/list.html'
    queryset = Category.objects.all()


class CategoryDetailView(DetailView):
    # This view displays all the posts which have category
    # related to

    model = Category
    template_name = 'post/category/detail.html'
    query_pk_and_slug = True
    # default of slug_field and slug_url_kwarg also are 'slug'
    # so we don't need to set in this case

    def get_object(self):
        # replace objects.get() by objects.filter
        # cause the get function can not handle in the case 
        # more than 2 result returned
        return Category.objects.filter(slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # __in: return the post'category in the queryset
        context['title'] = self.kwargs[self.slug_url_kwarg]
        context['posts'] = Post.objects.filter(category__in=self.get_object())

        return context


class PostCreateView(CreateView):

    model = Post
    # form_class = forms.PostCreateForm
    fields = '__all__'
    template_name = 'post/post/create.html'


class PostListView(ListView):

    model = Post
    template_name = 'post/post/list.html'
    queryset = Post.objects.all()


class PostDetailView(DetailView):

    model = Post
    template_name = 'post/post/detail.html'
    # slug_field = 'slug'
    # slug_url_kwarg = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)


        # get commetn related to this post
        # in order by date
        comments = Comment.objects.filter(post=self.get_object()).order_by('date')
        # add the query to the current context
        context['comments'] = comments
        context['comment_form'] = forms.CommentCreateForm()

        return context

    def post(self, request, *arg, **kwargs):

        if self.request.user.is_anonymous:
            new_comment = Comment( content=request.POST.get('content'),
                                post=self.get_object()
                            )    
        else:
            new_comment = Comment( content=request.POST.get('content'),
                                author=self.request.user.username,
                                post=self.get_object()
                            )
        new_comment.save()
        return self.get(self, request,*arg, **kwargs)
