from django.shortcuts import render
from django.views.generic import ListView

from apps.post.models import Post

from itertools import chain 


class SearchView(ListView):

    template_name = 'base/search.html'

    def get_queryset(self):
                # split the input text into words
        queries = self.request.GET.get('search', None)
        if queries is not None:
            queries = queries.split()
            for query in queries:

                if query is not None:
                    posts = Post.objects.filter(title__contains=query)

                    return posts

        return Post.objects.none()


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        return context

