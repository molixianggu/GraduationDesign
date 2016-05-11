from django import forms

from managementSystem.models import *

from django.core.exceptions import ValidationError


def User_presence(value):
    if Admin.objects.filter(userName = value)[:1]:
        raise ValidationError('该用户名已经存在')

class RegisterForm(forms.Form):
    nickName = forms.CharField(
      max_length=32,
        label = '昵称'
    )
    userName = forms.CharField(
      max_length=30,
        label = '用户名',
        validators=[
          User_presence,
        ]
    )
    passWord = forms.CharField(
      max_length=32,
      label='密码',
      widget=forms.PasswordInput(),
    )
    repPassWord = forms.CharField(
      max_length=32,
      label='确认',
      widget=forms.PasswordInput(),
    )
#    question = forms.ChoiceField(
    #        widget=forms.RadioSelect,
    #        label = '密码问题',
#        choices=(
    #            ('0', 'abcde'),
#            ('1', 'bdeee'),
#            ('2', 'python'),
#            ('3', 'java')
#        )
#    )
    answer = forms.CharField(
      max_length=50,
        label = '答案'
    )


class importReport(forms.Form):
  file = forms.FileField()


class UpLoadForm(forms.Form):
    DirectParent = forms.CharField(
        max_length=32,
        label = '父节点',
    )
    templatePositions = forms.FileField(
        label=''
    )
    templateName = forms.CharField(
        max_length=32,
        label='名称'
    )

