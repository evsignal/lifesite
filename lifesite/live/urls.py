from django.conf.urls import url

from . import views


#app_name = 'live'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]

'''
    # ex: /live/
    url(r'^$', views.index, name='index'),
    # ex: /live/number_article
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail')
'''