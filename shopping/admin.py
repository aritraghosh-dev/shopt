from django.contrib import admin
from shopping.models import product,catagory

class Adminproduct(admin.ModelAdmin):
    list_display=['name','price','cat']

admin.site.register(product,Adminproduct)
admin.site.register(catagory)
