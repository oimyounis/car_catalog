# Generated by Django 2.1.2 on 2018-10-30 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181030_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='parents',
            field=models.ManyToManyField(blank=True, related_name='children', to='products.Category'),
        ),
        migrations.AlterField(
            model_name='producttypefield',
            name='type',
            field=models.IntegerField(choices=[(1, 'Text'), (2, 'Long Text'), (3, 'Number'), (4, 'Multi Value'), (5, 'File'), (6, 'Image'), (7, 'Multi Image')], default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.ProductType'),
        ),
    ]
