from django.contrib import admin
from .models import Category, ProductType, ProductTypeField, ProductTypeFieldChoice


admin.site.register(Category)


class FieldsInline(admin.TabularInline):
    model = ProductTypeField


class ChoicesInline(admin.StackedInline):
    model = ProductTypeFieldChoice


class ProductTypeFieldAdmin(admin.ModelAdmin):
    inlines = [
        ChoicesInline,
    ]

    class Media:
        js = ('products/js/product_type_field.js',)
        css = {'all': ['products/css/product_type_field.css']}


admin.site.register(ProductTypeField, ProductTypeFieldAdmin)
admin.site.register(ProductType)
