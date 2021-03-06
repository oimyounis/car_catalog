# Generated by Django 2.0.6 on 2018-10-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(1, 'Text'), (2, 'Long Text'), (3, 'Number'), (4, 'Drop Down'), (5, 'Check Box'), (6, 'Radio Button'), (7, 'File'), (8, 'Image')])),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='parents',
            field=models.ManyToManyField(blank=True, null=True, related_name='children', to='products.Category'),
        ),
    ]
