from django.contrib import admin
from shopping.models import product,catagory,order

class Adminproduct(admin.ModelAdmin):
    list_display=['name','price','cat']

admin.site.register(product,Adminproduct)
admin.site.register(catagory)
admin.site.register(order)
