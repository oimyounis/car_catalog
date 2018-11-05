from django.http.response import HttpResponse
from django.template.loader import get_template
from .models import ProductType, FieldType


def generate_product_fields_form(request, product_type_id):
    product_type = ProductType.objects.filter(pk=product_type_id).first()

    pt_fields = product_type.fields.all()

    rendered = get_template('products/products_partial_form.html').render({'fields': pt_fields, 'FieldType': FieldType})

    return HttpResponse(rendered)
