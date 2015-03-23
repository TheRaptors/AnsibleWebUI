from django.conf.urls import patterns, url
from Hosts import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^host/add/$', views.hostadd, name='hostadd'),
                       url(r'^host/list/$', views.hostlist, name='hostlist'),
                       url(r'^host/(?P<hostopt>[\w]+)/(?P<hostid>[\d]+)/$', views.hostOpt, name='hostOpt'),
                       url(r'^group/(?P<groupopt>[\w]+)/(?P<gid>[\d]{0,})', views.groupOpt, name='groupOpt'),
                       # url(r'^playbook/$', views.playbook, name='playbook'),
                       # url(r'^dcelery/$', views.dcelery, name='dcelery'),
)
