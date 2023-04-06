from django.shortcuts import render, get_object_or_404
from .models import Category, News
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    categories = Category.objects.all()
    news_list = News.objects.order_by('-created_date')

    # filter by category
    category_id = request.GET.get('category')
    category_url = None
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        news_list = news_list.filter(category=category)
        category_url = category.slug

    # filter by date
    date = request.GET.get('date')
    if date:
        news_list = news_list.filter(created_date__date=date)

    paginator = Paginator(news_list, 3)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'news/home.html', {'news': news, 'categories': categories, 'category_url': category_url})


def category(request, slug=None):
    if slug:
        category = get_object_or_404(Category, slug=slug)
        news_list = category.news.order_by('-created_date')
    else:
        # category = None
        news_list = News.objects.none()
    categories = Category.objects.all()
    paginator = Paginator(news_list, 10)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    return render(request, 'news/category.html', {'news': news, 'categories': categories})


def category_view(request, slug):
    category_slugs = slug.split('/')
    main_category_slug = category_slugs[0]
    subcategory_slug = category_slugs[1]
    news_list = News.objects.order_by('-created_date')
    main_category = get_object_or_404(Category, slug=main_category_slug)
    subcategory = get_object_or_404(Category, slug=subcategory_slug, parent=main_category)

    news = subcategory.news.order_by('-created_date')
    categories = Category.objects.all()

    context = {
        'main_category': main_category,
        'subcategory': subcategory,
        'news': news,
        'news_list': news_list,
        'categories': categories,
    }
    return render(request, 'news/category.html', context)


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})
