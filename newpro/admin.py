from django.contrib import admin
from .models import destination,Products, Contact
# Register your models here.


# admin.site.register(destination)

@admin.register(destination)
class destinationAdmin(admin.ModelAdmin):
    list_display = ("title",  "desc")
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("title",  "desc")
# @admin.register(Products)

admin.site.register(Contact)





