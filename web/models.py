from django.db import models

# Create your models here.
#用户实体类
class Customers(models.Model):
    tel = models.BigIntegerField(verbose_name='电话号码')
    pwd = models.CharField(max_length=30, verbose_name='密码')
    email = models.EmailField(verbose_name='电子邮件')
    name = models.CharField(max_length=20,verbose_name='用户名')
    isActive = models.BooleanField(default=True, verbose_name='激活/禁用')
    def __str__(self):
        return self.name
    def __repr__(self):
        return '<Customer:%r'%self.name
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name