from django.urls import path
from . import apiviews


app_name = "products_api"

urlpatterns = [
    path('product_fields_form/<int:product_type_id>', apiviews.generate_product_fields_form, name='generate_product_fields_form'),
]
