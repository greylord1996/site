from django.http import  Http404
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator, InvalidPage
from shop.models import Category, Good
from django.views.generic.base import ContextMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.edit import ProcessFormView
from django.urls import reverse

class CategoryListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        context["cats"] = Category.objects.order_by("name")
        return context

class GoodListView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super(GoodListView, self).get_context_data(**kwargs)
        try:
            page_num = self.request.GET["page"]
        except KeyError:
            page_num = 1
        context["cats"] = Category.objects.order_by("name")
        if kwargs["cat_id"] == None:
            context["category"] = Category.objects.first()
        else:
            context["category"] = Category.objects.get(pk = kwargs["cat_id"])
        paginator = Paginator(Good.objects.filter(category=context["category"]).order_by("name"), 5)
        try:
            context["goods"] = paginator.page(page_num)
        except InvalidPage:
            context["goods"] = paginator.page(1)
        return context


class GoodDetailView(TemplateView):
    template_name = "good.html"
    def get_context_data(self, **kwargs):
        context = super(GoodDetailView, self).get_context_data(**kwargs)
        try:
            context["good"] = Good.objects.get(pk=kwargs["id"])
        except Good.DoesNotExist:
            raise Http404("Вы кто такие? Я вас не звал.")
        context["cats"] = Category.objects.order_by("name")
        return context


class GoodEditMixin(CategoryListMixin):
    def get_context_data(self, **kwargs):
        context = super(GoodEditMixin, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except KeyError:
            context["pn"] = 1
        return context

class GoodEditView(ProcessFormView):
    def post(self, request, *args, **kwargs):
        try:
            pn = request.GET["page"]
        except KeyError:
            pn = "1"
        self.success_url = self.success_url + "?page" + pn
        return super(GoodEditView, self).post(request, *args, **kwargs)

class GoodCreate(CreateView, GoodEditMixin):
    model = Good
    fields = '__all__'
    template_name = "good_add.html"
    def get(self, request, *args, **kwargs):
        if self.kwargs["cat_id"] != None:
            self.initial["category"] = Category.objects.get(pk=self.kwargs["cat_id"])
        return super(GoodCreate, self).get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        self.success_url = reverse("index", kwargs={"cat_id": Category.objects.get(pk=self.kwargs["cat_id"]).id})
        return super(GoodCreate, self).post(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(GoodCreate, self).get_context_data(**kwargs)
        context["category"] = Category.objects.get(pk=self.kwargs["cat_id"])
        return context

class GoodUpdate(UpdateView, GoodEditMixin, GoodEditView):
    model = Good
    fields = '__all__'
    template_name = "good_edit.html"

    pk_url_kwarg = "id"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("index", kwargs={"cat_id": Good.objects.get(pk=kwargs["id"]).category.id})
        return super(GoodUpdate, self).post(request, *args, **kwargs)









