# coding:utf8
__author__ = 'zhaifg'
from Hosts.models import *
from django import forms


class GroupForm(forms.ModelForm):
    gname = forms.CharField(max_length=128, label=u"组名称", error_messages={'required': u'请输入字母'})
    description = forms.CharField(widget=forms.Textarea, label=u"说明")

    class Meta:
        model = Group
        fields = ['gname','description']


class HostForm(forms.ModelForm):
    ipaddr = forms.IPAddressField(label=u'IP地址', required=True, help_text=u'主机的IP地址')
    user = forms.CharField(max_length=128, label=u'登录用户', help_text=u'登录主机的用户名,默认为root')
    password = forms.CharField(max_length=128, label=u'登录密码')
    group = forms.ModelChoiceField(queryset=Group.objects.all(), label=u'选择相应的组')

    class Meta:
        model = Host
        fields = ['ipaddr', 'user', 'password','group']







