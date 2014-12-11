from django.conf.urls import patterns, include, url

from kevin_liao_website.urls import *

from blog import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name='index'), 
        # ex: /blog/5
        url(r'^(?P<post_id>\d+)/$', views.post, name='post'),
        url(r'^archive/', views.archive, name='archive'),
)
