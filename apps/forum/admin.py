from django.contrib import admin

from . import models

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SubcategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)

admin.site.register(models.Category, CategoriesAdmin)
admin.site.register(models.Subcategory, SubcategoriesAdmin)
