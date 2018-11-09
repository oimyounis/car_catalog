from django.contrib import admin
from .models import Category, ProductType, ProductTypeField, ProductTypeFieldChoice, Product, FieldType, ProductMultiValueFieldValue, ProductTextFieldValue, ProductFileFieldValue, ProductImageFieldValue


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
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        ProductTextFieldValue.objects.filter(product=obj).delete()
        ProductMultiValueFieldValue.objects.filter(product=obj).delete()
        ProductFileFieldValue.objects.filter(product=obj).delete()
        ProductImageFieldValue.objects.filter(product=obj).delete()

        for field in request.POST:
            if 'field_' in field:
                field_parts = field.split('_')
                type = field_parts[2]
                id = field_parts[1]
                if int(type) == int(FieldType.MULTI_VALUE):
                    for value in request.POST.getlist(field):
                        ProductMultiValueFieldValue(product=obj, field=ProductTypeField.objects.get(id=id), value=ProductTypeFieldChoice.objects.get(id=value)).save()
                elif int(type) not in (int(FieldType.IMAGE), int(FieldType.FILE)):
                    ProductTextFieldValue(product=obj, field=ProductTypeField.objects.get(id=id), value=request.POST.get(field)).save()

        for field in request.FILES:
            if 'field_' in field:
                field_parts = field.split('_')
                type = field_parts[2]
                id = field_parts[1]

                if int(type) == int(FieldType.FILE):
                    ProductFileFieldValue(product=obj, field=ProductTypeField.objects.get(id=id), value=request.FILES.get(field)).save()
                elif int(type) == int(FieldType.IMAGE):
                    ProductImageFieldValue(product=obj, field=ProductTypeField.objects.get(id=id), value=request.FILES.get(field)).save()
                elif int(type) == int(FieldType.MULTI_IMAGE):
                    for value in request.FILES.getlist(field):
                        ProductImageFieldValue(product=obj, field=ProductTypeField.objects.get(id=id), value=value).save()

    class Media:
        js = ('products/js/reverse.js', 'products/js/product_admin_form_generator.js',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductTypeField, ProductTypeFieldAdmin)
admin.site.register(ProductType)
admin.site.register(Product, ProductAdmin)
