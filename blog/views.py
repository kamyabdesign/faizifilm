# from django.views.generic import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

from .models import Article, Category, Tag, Comments
from work.models import Work
from . forms import CommentForm


def blog(request):
    blogs = Article.objects.filter(status="p").order_by('-publish')

    paginator = Paginator(blogs, 8)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)
    context = {
        'blogs': paged_post
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, slug):
    post_detail = get_object_or_404(Article, slug=slug)
    work = Work.objects.order_by('-created')[:4]
    category = Category.objects.all()
    tags = Tag.objects.all().filter(blogs=post_detail)
    recent = Article.objects.filter(status="p").order_by(
        '-created').exclude(slug=slug)[:3]
    comments = Comments.objects.all().filter(blog=post_detail)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_message = form.cleaned_data['message']

            new_comment = Comments(
                blog=post_detail, name=new_name, email=new_email, message=new_message)
            new_comment.save()

    context = {
        'post_detail': post_detail,
        'recent': recent,
        'work': work,
        'category': category,
        'tags': tags,
        'comments': comments
    }
    return render(request, 'blog/blog_detail.html', context)


def blog_tag(request, tag):
    blogs = Article.objects.filter(tag__slug=tag)

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)


def blog_category(request, category):
    blogs = Article.objects.filter(category__slug=category)
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blog.html', context)


def search(request):
    queryset = Article.objects.all()
    query_set = Work.objects.all()

    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    context = {
        'queryset': queryset,
        'query_set': query_set
    }

    return render(request, 'blog/search.html', context)
