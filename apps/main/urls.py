from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^success$', views.success),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^new_product/(?P<id>\d+)$', views.new_product),
    url(r'^new_product_page/$', views.new_product_page),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^logout$', views.logout)



]
