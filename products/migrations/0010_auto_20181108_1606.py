# Generated by Django 2.1.2 on 2018-11-08 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_productfilefieldvalue_productimagefieldvalue_productmultivaluefieldvalue_producttextfieldvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmultivaluefieldvalue',
            name='value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductTypeFieldChoice'),
        ),
    ]
