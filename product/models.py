from django.db import models

# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CategoryModel(TimeStampModel):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class ProductModel(TimeStampModel):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        CategoryModel, on_delete=models.CASCADE, related_name="category_product"
    )
    price = models.FloatField()
    image = models.ImageField(blank=True, upload_to="static/")
