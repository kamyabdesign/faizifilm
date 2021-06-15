from django.shortcuts import render
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from .models import Work
from blog.models import Category
from film.models import Video


def working(request):
    work = Work.objects.all().order_by('-created')
    category = Category.objects.all()

    paginator = Paginator(work, 6)
    page = request.GET.get('page')
    paged_work = paginator.get_page(page)
    context = {
        'work': paged_work,
        'category': category,

    }
    return render(request, 'work/work.html', context)


def work_detail(request, slug):
    detail = get_object_or_404(Work, slug=slug)
    recent = Work.objects.all().exclude(slug=slug)[:3]
    category = Category.objects.all()
    video = Video.objects.all().order_by('-create')[:2]
    context = {
        'detail': detail,
        'recent': recent,
        'category': category,
        'video': video,
    }
    return render(request, 'work/work_detail.html', context)


def work_category(request, category):
    work = Work.objects.filter(category__slug=category)
    context = {
        'work': work
    }
    return render(request, 'work/work.html', context)
