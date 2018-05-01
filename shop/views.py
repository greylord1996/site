from django.shortcuts import render
from django.http import HttpResponse, Http404
from shop.models import Good, Category
from django.core.paginator import Paginator
from django.core.paginator import InvalidPage

"""
def list(request):
    return HttpResponse("Page doesn't exist")
"""
def index(request, cat_id):
    try:
        page_num = request.GET["page"]
    except KeyError:
        page_num = 1
    cats = Category.objects.all().order_by("name")
    if cat_id == None:
        cat = Category.objects.first()
    else:
        cat = Category.objects.get(pk=cat_id)
    paginator = Paginator(Good.objects.filter(category=cat).order_by("name"), 5)
    try:
        goods = paginator.page(page_num)
    except InvalidPage:
        goods = paginator.page(1)
    return render(request, "index.html", context={'category': cat, 'cats': cats, 'goods': goods})

def good(request, id):
    cats = Category.objects.all().order_by("name")
    try:
        good = Good.objects.get(pk=id)
    except Good.DoesNotExist:
        raise Http404("Вы кто такие? Я вас не звал.")
    s = good.name + "<br><br>" + good.category.name + "<br><br>" + good.description
    if not good.in_stock:
        s = s + "<br><br>" + "Нет в наличии"
    return render(request, 'good.html', context={'cats': cats, 'good': good})






