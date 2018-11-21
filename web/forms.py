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