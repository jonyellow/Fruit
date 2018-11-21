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

#商品类型
class GoodsType(models.Model):
    title = models.CharField(max_length=50, verbose_name='类型名称')
    picture = models.ImageField(upload_to='img' ,null=True, blank=True)
    desc = models.TextField(verbose_name='类型描述')
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'goods_type'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name
    def to_dict(self):
        dic = {
            'title': self.title,
            'desc': self.desc,
        }
        return dic

#商品信息
class Goods(models.Model):
    title = models.CharField(max_length=50, verbose_name='商品名称')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='商品价格')
    picture = models.ImageField(upload_to='img', null=True, blank=True)
    spec = models.CharField(max_length=20, verbose_name='商品规格')
    #创建于商品类型的多对一关系
    goodsType = models.ForeignKey(GoodsType, verbose_name='商品类型', on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True, verbose_name='是否上架')
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
    def to_dict(self):
        dic = {
            'title': self.title,
            'price': self.price,
            'spec': self.spec,
            'goodsType': self.goodsType,
            'isActive': self.isActive,
        }
        return dic