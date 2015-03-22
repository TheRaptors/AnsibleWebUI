#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Hosts.forms import *
from Hosts.models import *

PORT = (80, 8080, 11211, 3306)
def index(request):
    pass


def hostlist(request):
    context_dict = {}
    hosts = Host.objects.all()[:10]
    context_dict['hosts'] = hosts

    return render(request, "host/hostlist.html", context_dict)


def hostadd(request):
    context_dict = {}
    if request.method == 'POST':
        # 没有进行验证, 提交验证,密码加密存储
        ipaddr = request.POST['ipaddr'].strip()
        user = request.POST['user'].strip()
        password = request.POST['password'].strip()
        g = request.POST['group'].strip()
        group = Group.objects.get_or_create(cname=g)[0]
        host = Host()
        host.ipaddr=ipaddr
        host.user = user
        host.password = password
        host.group = group
        host.save()

        return HttpResponseRedirect("/Hosts/host/list/")


    elif request.method == 'GET':
        context_dict['group'] = Group.objects.all()
        return render(request, "host/hostadd.html", context_dict)



def hostopt(request, hostopt, hostid):
    context_dict = {}
    try:
        host = Host.objects.get(id=hostid)

    except Exception, e:
        print str(e)

    if "view" == hostopt:
        context_dict["host"] = host
        return render(request, "host/hostview.html", context_dict)
    elif "edit" == hostopt:

        try:
            hostname = None
            user = ""
            password = ""


            host.hostname = hostname
            host.user = user
            host.password = password

            host.save()
            context_dict["host"] = host
            return render(request, "host/hostview.html", context_dict)
        except Exception, e:
            print str(e)
    elif "del" == hostopt:
        host.delete()
        return HttpResponseRedirect("/Hosts/host/list/")

