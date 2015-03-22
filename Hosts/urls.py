from django.conf.urls import patterns, url
from Hosts import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^host/add/$', views.hostadd, name='hostadd'),
                       url(r'^host/list/$', views.hostlist, name='hostlist'),
                       url(r'^host/(?P<hostopt>[\w]+)/(?P<hostid>[\d]+)/$', views.hostopt, name='hostopt'),
                       # url(r'^playbook/$', views.playbook, name='playbook'),
                       # url(r'^dcelery/$', views.dcelery, name='dcelery'),
)
