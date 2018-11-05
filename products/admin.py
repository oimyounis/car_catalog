from django.contrib import admin
from .models import Category, ProductType, ProductTypeField, ProductTypeFieldChoice, Product


class FieldsInline(admin.TabularInline):
    model = ProductTypeField


class ChoicesInline(admin.StackedInline):
    model = ProductTypeFieldChoice


class ProductTypeFieldAdmin(admin.ModelAdmin):
    inlines = [
        ChoicesInline,
    ]

    list_display = ('title', 'product_type')

    class Media:
        js = ('products/js/product_type_field.js',)
        css = {'all': ['products/css/product_type_field.css']}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


class ProductAdmin(admin.ModelAdmin):
    class Media:
        js = ('products/js/reverse.js', 'products/js/product_admin_form_generator.js',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductTypeField, ProductTypeFieldAdmin)
admin.site.register(ProductType)
admin.site.register(Product, ProductAdmin)
