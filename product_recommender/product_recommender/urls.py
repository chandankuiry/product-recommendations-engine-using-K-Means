from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'product_recommender.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^reviews/', include('reviews.urls', namespace="reviews")),
    url(r'^admin/', include(admin.site.urls)),
]
