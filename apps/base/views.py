from django.shortcuts import render
from django.views.generic import ListView

from apps.post.models import Post, Category
from apps.user.models import UserProfile

from itertools import chain 


class SearchView(ListView):

    template_name = 'base/search.html'

    def get_queryset(self):
        pass

    def search(self):
        queries = self.request.GET.get('search', None)
        posts = Post.objects.none()
        cats = Category.objects.none()
        users = UserProfile.objects.none()
        print('[Search Engine]', queries)

        if queries is not None:
            queries = queries.split()
            for query in queries:

                if query is not None:
                    posts = chain(posts, Post.objects.filter(title__contains=query))
                    cats = chain(cats, Category.objects.filter(name__contains=query))
                    users = chain(users, UserProfile.objects.filter(username__contains=query))

        data = {
            'posts': posts,
            'categories': cats,
            'users': users,
        }

        return data

    def is_empty_result(self, search_result):
        for key in search_result:
            if any(search_result[key]):
                return False
        print('[Search Engine] Empty Result')
        return True

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        search_result = self.search()
        context.update(search_result)
        context['is_empty_result'] = self.is_empty_result(search_result)
        print(f'[Search] Context\n', context)
        print('='*30)

        return context 


class HomeView(ListView):

    template_name = 'base/home.html'

    def get_queryset(self):
        # will be error if queryset/get_queryset() is not set
        pass
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # add more data to display on the home page
        context['posts'] = Post.objects.all().order_by('date')[:10]
        context['categories'] = Category.objects.all()[:10]

        return context


