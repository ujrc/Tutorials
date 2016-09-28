from django.conf.urls import  include, url
from rest_framework.routers import DefaultRouter

from webtweets.api.views import TweetViewSet,UserViewSet


router = DefaultRouter()
router.register(r'tweets',TweetViewSet,base_name='tweets-list')
router.register(r'users', UserViewSet,base_name='user-list')

urlpatterns =[
    url(r'^api/', include(router.urls)),

]