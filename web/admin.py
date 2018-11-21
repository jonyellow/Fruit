from django.contrib import admin
from .models import *
# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'spec')
    search_fields = ('title',)
    list_filter = ('goodsType',)

admin.site.register(GoodsType)
admin.site.register(Goods, GoodsAdmin)
