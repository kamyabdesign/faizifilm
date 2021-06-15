from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Main, Hestory, Video, Team, Trust, Testimonial, Features, our_service


from blog.models import Article
from work.models import Work


def index(request):
    main = Main.objects.all()
    hes_tory = Hestory.objects.all()
    team = Team.objects.all()
    trust = Trust.objects.all()
    film = Video.objects.all()
    work = Work.objects.order_by("-created")[:4]
    testimonial = Testimonial.objects.all()
    article = Article.objects.filter(status="p").order_by("-publish")[:3]

    context = {
        'main': main,
        'hes_tory': hes_tory,
        'team': team,
        'film': film,
        'trust': trust,
        'testimonial': testimonial,
        'article': article,
        'work': work,
    }
    return render(request, 'film/index.html', context)


def video(request):
    films = Video.objects.all().order_by("-create")

    paginator = Paginator(films, 8)
    page = request.GET.get('page')
    paged_post = paginator.get_page(page)

    context = {
        'films': paged_post
    }

    return render(request, 'film/video.html', context)


def about(request):
    service = our_service.objects.all()
    feature = Features.objects.all()
    trust = Trust.objects.all()
    work = Work.objects.order_by("-created")[:2]
    team = Team.objects.all()

    context = {
        'service': service,
        'feature': feature,
        'trust': trust,
        'work': work,
        'team': team

    }
    return render(request, 'film/about.html', context)
