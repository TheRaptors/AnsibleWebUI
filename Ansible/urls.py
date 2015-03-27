__author__ = 'zhaifg'
from django.conf.urls import patterns, url
from Ansible import views

urlpatterns = patterns('',
                       #url(r'^$', views.index, name="index"),
                       #url(r'^runmodule/$', views.runmodule, name='runmodule'),
                       #url(r'^runplaybook/$', views.runplaybook, name='runplaybook'),
                      # url(r'^playbook/$', views.playbook, name='playbook'),
                      # url(r'^dcelery/$', views.dcelery, name='dcelery'),
                       url(r'^pblist/$', views.pblist, name='pblist'),
)