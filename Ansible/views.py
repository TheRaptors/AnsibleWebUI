from django.shortcuts import render
from django.http import HttpResponse
from ansible.inventory import Inventory
from ansible.playbook import PlayBook
import ansible.runner
import json
import time
import ansible.playbook
from ansible import callbacks
from ansible import utils
import ansible.constants as C
from Ansible import tasks_self
import random


class Stdout:
    def __init__(self, hostname, stdout):
        self.hostname = hostname
        self.stdout = json.dumps(stdout, indent=4)


    # def getjosn(self, stdout):
    #     return json.dumps(stdout, indent=4)

    @property
    def formatJson(self):
        std = self.stdout.replace("\n","<br>").replace(' ','&nbsp;')
        return std

def index(request):
    # result = tasks.add.delay(random.randint(1,5),4)
    # print result.result
    # print  result.status
    # time.sleep(5)
    #
    # if result.ready():
    #     print "Task has Run"
    #     if result.successful():
    #         print "Result was: %s"% result.result
    #     else:
    #         if isinstance(result.result, Exception):
    #             print "Task failed without raising exception"
    # else:
    #     print "Task has not yet run"
    return render(request,"ansible/runmodule.html",{})


def dcelery(request):
    result = tasks_self.add.delay(random.randint(1, 5), 5)
    print result.status
    print "--------------->"
    print result.get()
    #time.sleep(5)
    if result.ready():
        print "Task has Run ......"
        print result.successful
        if result.successful():
            res = result.result
            print "Result was: %s"% res

            return HttpResponse(res)
        else:
            print result.status
            if isinstance(result.result, Exception):
                print "Task failed without raising exception"

    else:
        print "Task has not yet run"

    return HttpResponse("Null")


def playbook(request):
    return render(request, "ansible/runplaybook.html", {})


def runmodule(request):
    context_dict = {}
    inventory = request.POST['inventory']
    a = request.POST['inventory']+"------->"+request.POST["module"]+ "------------>" + request.POST['args']+request.POST["others"]

    # results = ansible.runner.Runner(
    #     pattern=inventory,
    #     module_name=request.POST['module'],
    #     module_args=request.POST['args'],
    # ).run()


    rsts = tasks_self.modrun.delay(inventory, request.POST['module'], request.POST['args'])
    results = rsts.get()
    stdout = []
    failed = []
    down = []
    if results is None:
        stdout = None
        failed = None
        down = None

    stdout.append("UP  *********************")
    print "UP ----------------------------------"
    for (hostname, result) in results['contacted'].items():
        if not 'failed' in result:
            #print "%s >>> %s" % (hostname, result['stdout'])
            #stdout.append("%s >>> %s"%(hostname, result['stdout']))
            std = Stdout(hostname, result)
            stdout.append(std)
            print std.hostname
            print type(std.stdout)
            #print std.stdout
            print std.formatJson

    context_dict["stdout"] = stdout

    print "FAILED -----------------------------"
    failed.append("FAILED  ******************")
    for (hostname, result) in results['contacted'].items():
        if 'failed' in result:
            print "%s >>> %s" % (hostname, result['msg'])
            failed.append("%s >>> %s"%(hostname, result['msg']))

    context_dict["failed"] = failed

    print "DOWN ------------------------------"
    down.append("DOWN *******************")
    for (hostname, result) in results['dark'].items():
        print "%s >>> %s" % (hostname, result)
        dw = Stdout(hostname, result)
        down.append(dw)

    context_dict["down"] = down

    context_dict['a'] = a
    print a

    #return HttpResponse(a)

    return render(request, "ansible/runresults.html", context_dict)

def runplaybook(request):

    context_dict= {}
    stats = callbacks.AggregateStats()
    playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    runner_cb = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)
    yml = "/home/zhaifg/development/EasyOPT/ansible/ec/"+request.POST['playbook'].strip()
    hosts = "/home/zhaifg/development/EasyOPT/ansible/ec/hosts"
    res = ansible.playbook.PlayBook(
    host_list=hosts,
    playbook=yml,
    stats=stats,
    callbacks=playbook_cb,
    runner_callbacks=runner_cb,
    check=False
).run()
    start= "RCOPY PLAY:*************************************************"

    stdout = [start]

    for key in res.keys():
       st = ''
       for kk in res[key].keys():
           st += kk+"="+str(res[key][kk])+"\t"
           a = key + ":\t" + st
       print a
       stdout.append(a)
       context_dict['stdout'] = stdout

    return render(request, 'ansible/playbookres.html',context_dict)
