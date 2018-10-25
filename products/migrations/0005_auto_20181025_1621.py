# Generated by Django 2.0.6 on 2018-10-25 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20181025_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttypefield',
            name='choices',
        ),
        migrations.AddField(
            model_name='producttypefieldchoice',
            name='product_type_field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='products.ProductTypeField'),
        ),
    ]
