from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    parents = models.ManyToManyField('self', 'children', symmetrical=False, null=True, blank=True)

    def __str__(self):
        return self.name


class FieldType:
    TEXT = 1
    LONG_TEXT = 2
    NUMBER = 3
    SELECT = 4
    CHECKBOX = 5
    RADIOBUTTON = 6
    FILE = 7
    IMAGE = 8

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class ProductTypeField(models.Model):
    type = models.IntegerField(choices=(
        (FieldType.TEXT, 'Text'),
        (FieldType.LONG_TEXT, 'Long Text'),
        (FieldType.NUMBER, 'Number'),
        (FieldType.SELECT, 'Select'),
        (FieldType.CHECKBOX, 'Check Box'),
        (FieldType.RADIOBUTTON, 'Radio Button'),
        (FieldType.FILE, 'File'),
        (FieldType.IMAGE, 'Image')
    ), default=FieldType.TEXT)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='fields')
    title = models.CharField(max_length=255)
    tip = models.CharField(max_length=255, null=True, blank=True)


class ProductTypeFieldChoice(models.Model):
    name = models.CharField(max_length=255, null=True)
    product_type_field = models.ForeignKey(ProductTypeField, on_delete=models.CASCADE, related_name='choices', null=True)
