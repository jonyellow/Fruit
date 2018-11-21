from django import forms
from .models import *

class CusForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['tel', 'pwd']
        labels = {
            'tel': '电话号码',
            'pwd':'密码',
        }
        widgets = {
          'tel':forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
          'pwd': forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder': '请输入6-20位的字符',
                }
            )
        }
#用于注册：
class RegForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['tel','name', 'email', 'pwd']
        labels = {
            'tel': '电话号码',
            'name': '用户名',
            'email': '邮箱',
            'pwd':'密码',
        }
        widgets = {
          'tel':forms.NumberInput(
                attrs={
                    'class':'form-control'
                }
            ),
          'pwd': forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder': '请输入6-20位的字符',
                }
            ),
          'email': forms.EmailInput(
              attrs={
                  'class':'form-control',
                  'placeholder':'请输入邮箱',
              }
          ),
          'name': forms.TextInput(
              attrs={
                  'class':'form-control',
                  'placeholder':'请输入用户名',
              }
          ),
        }