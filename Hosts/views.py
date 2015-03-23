#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from Hosts.forms import *
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


def hostOpt(request, hostopt, hostid):
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



def groupOpt(request, groupopt, gid=None):

    context_dict = {}
    if groupopt == "add" and not gid:
        if request.method == 'GET':
            return render(request,"host/groupadd.html",{})
        elif request.method == "POST":
            cname = request.POST['cname'].strip()
            if cname == "":
                pass
            description = request.POST['description'].strip()
            g = Group()
            g.cname = cname
            g.description = description
            g.save()
            return HttpResponseRedirect("/Hosts/group/list/")
        else:
            return HttpResponseRedirect("/Hosts/group/list/")

    elif groupopt == "list" and not gid:
        group = Group.objects.all()
        context_dict['group'] = group
        return render(request, 'host/grouplist.html', context_dict)

    elif groupopt != 'add' and groupopt != "list" and gid:
        g = Group.objects.filter(id=long(gid))
        if len(g) == 0:
            pass
        else:
            if groupopt == 'del':
                g.delete()
                return  HttpResponseRedirect('/Hosts/group/list')
            elif groupopt == "edit":
                context_dict['group'] = g[0]
                if request.method ==  'GET':
                    print g[0].cname
                    return render(request,'host/groupview.html', context_dict)
                elif request.method == 'POST':
                    g = Group.objects.filter(id=long(request.POST['gid']))[0]
                    g.cname = request.POST['cname'].strip()
                    g.description = request.POST['description'].strip()
                    g.save()
                    return HttpResponseRedirect('/Hosts/group/list')

    else:
        return  HttpResponseRedirect('/Hosts/group/list/')


