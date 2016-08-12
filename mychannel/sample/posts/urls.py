from django.conf.urls import url 
from . views import index, my_blog

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<slug>[^/]+)/$',my_blog, name='blog'),
    ]
  
