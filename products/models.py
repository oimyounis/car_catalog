from django.db import models


class FieldType:
    TEXT = 1
    LONG_TEXT = 2
    NUMBER = 3
    MULTI_VALUE = 4
    FILE = 5
    IMAGE = 6
    MULTI_IMAGE = 7

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    parents = models.ManyToManyField('self', 'children', symmetrical=False, blank=True)

    @property
    def parent(self):
        allcats = [cat for cat in self.parents.values_list('name', flat=True)]
        return ', '.join(allcats)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductTypeField(models.Model):
    type = models.IntegerField(choices=(
        (FieldType.TEXT, 'Text'),
        (FieldType.LONG_TEXT, 'Long Text'),
        (FieldType.NUMBER, 'Number'),
        (FieldType.MULTI_VALUE, 'Multi Value'),
        (FieldType.FILE, 'File'),
        (FieldType.IMAGE, 'Image'),
        (FieldType.MULTI_IMAGE, 'Multi Image'),
    ), default=FieldType.TEXT)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='fields')
    title = models.CharField(max_length=255)
    tip = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class ProductTypeFieldChoice(models.Model):
    text = models.CharField(max_length=255, null=True)
    product_type_field = models.ForeignKey(ProductTypeField, on_delete=models.CASCADE, related_name='choices', null=True)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)


class ProductTextFieldValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    field = models.ForeignKey(ProductTypeField, on_delete=models.SET_NULL, null=True, blank=True)
    value = models.TextField()


class ProductFileFieldValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    field = models.ForeignKey(ProductTypeField, on_delete=models.SET_NULL, null=True, blank=True)
    value = models.FileField(upload_to='products/files/')


class ProductImageFieldValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    field = models.ForeignKey(ProductTypeField, on_delete=models.SET_NULL, null=True, blank=True)
    value = models.ImageField(upload_to='products/images/')


class ProductMultiValueFieldValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    field = models.ForeignKey(ProductTypeField, on_delete=models.SET_NULL, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
