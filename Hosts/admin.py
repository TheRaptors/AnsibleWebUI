from django.contrib import admin
from Hosts.models import *

admin.site.register(Group)
#admin.site.register(Project)
class HostAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['ipaddr', 'created_by', 'updated_by']

admin.site.register(Host, HostAdmin)
admin.site.register(Category)
