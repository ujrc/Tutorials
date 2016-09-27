from django.conf.urls import include, url
from django.views.generic import TemplateView
from webtweets.api import views

urlpatterns = [
    url(r'^',TemplateView.as_view(template_name='webtweets/weather/indexweather.html'),name='weather-home'),
    url(r'^tweeter/$',views.index, name='index'),
    url(r'^angular/$',TemplateView.as_view(template_name='webtweets/udemy/tutorial.html'), name='angular'),
    url(r'^angular-tuto/$',TemplateView.as_view(template_name='webtweets/tutorial/angulartuto.html'), name='angular-tuto'),
    # url(r'^spa-ng/$',TemplateView.as_view(template_name='webtweets/udemy/spApp.html'), name='spa-ng'),
     url(r'^ng-book/$',TemplateView.as_view(template_name='webtweets/ngBook/chap1.html'), name='ng-book'),

]
