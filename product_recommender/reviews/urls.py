from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /Product/
    url(r'^Product$', views.Product_list, name='Product_list'),
    # ex: /Product/5/
    url(r'^Product/(?P<Product_id>[0-9]+)/$', views.Product_detail, name='Product_detail'),
    url(r'^Product/(?P<Product_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]