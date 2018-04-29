from django.shortcuts import render
from django.http import HttpResponse, Http404
from shop.models import Good, Category

def list(request):
    return HttpResponse("Page doesn't exist")

def index(request, cat_id):
    if cat_id is not None:
        try:
            cat = Category.objects.get(pk=cat_id)
        except cat.DoesNotExist:
            raise Http404
    else:
        cat = Category.objects.first()
        HttpResponse("Priveeeeeeeeeeeeeeet")
    try:
        goodsAll = Good.objects.filter(category=cat).order_by("name")
    except Good.DoesNotExist:
        raise Http404

    s = "Категория: " + cat.name +"<br><br>"

    for ggg in goodsAll:
        s = s + "(" + str(ggg.pk) + ") " + ggg.name + "<br>"

    #return HttpResponse(s)
    return render(request, 'index.html', context={'cat': cat, 'goodsAll': goodsAll})

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






