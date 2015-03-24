from django.db import models
import datetime



# class Project(models.Model):
#     name = models.CharField(max_length=128, unique=True)
#     scm = models.CharField(max_length=128)
#     description = models.TextField(max_length=1024,blank=True)



class Group(models.Model):
    gname = models.CharField(max_length=128, unique=True, blank = False)
    # prj = models.ForeignKey(Project)
    description = models.TextField(max_length=1024,blank=True)

    def __unicode__(self):
        return self.gname


class Category(models.Model):
    catname = models.CharField(max_length=128, unique=True, blank = False)
    port = models.IntegerField()


class Host(models.Model):
    ipaddr = models.IPAddressField(unique=True, blank=False)
    hostname = models.CharField(max_length=128,null=True, blank=True)
    user = models.CharField(max_length=128, blank=False, default="root")
    password = models.CharField(max_length=256, blank=False)
    is_sudo = models.BooleanField(default=False)
    cpuinfo = models.CharField(max_length=256, blank=True, null=True)
    meminfo = models.IntegerField(max_length=32, blank=True,null=True)
    device = models.CharField(max_length=256,blank=True, null=True)
    wip = models.IPAddressField(blank=True, null=True)
    category = models.ManyToManyField(Category, null=True)
    group = models.ForeignKey(Group)

    created_by = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.ipaddr

    def update(self):
        pass



