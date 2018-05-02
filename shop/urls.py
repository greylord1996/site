from django.urls import path, include
from django.conf.urls import url
from shop import views
from shop.twviews import GoodListView, GoodDetailView, GoodCreate, GoodUpdate
"""
urlpatterns = [
    #url(r'^(?: (?P<id>\d+)/)?$', views.index, name="index"),
    url(r'^(?P<cat_id>\d+)/$', views.index, name="index"),
    url(r'^good/(?P<id>\d+)/$', views.good, name="good"),
    #url(r'', views.list, name="list"),
]
"""
urlpatterns = [
    #url(r'^(?: (?P<id>\d+)/)?$', views.index, name="index"),
    url(r'^(?P<cat_id>\d+)/$', GoodListView.as_view(), name="index"),
    url(r'^good/(?P<id>\d+)/$', GoodDetailView.as_view(), name="good"),
    url(r'^(?P<cat_id>\d+)/add/$', GoodCreate.as_view(), name="good_add"),
    url(r'^good/(?P<id>\d+)/edit/$', GoodUpdate.as_view(), name="good_edit"),
    #url(r'', views.list, name="list"),
]