from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    name_it = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    name_it = models.CharField(max_length=100)

    cost = models.FloatField()

    labels = models.JSONField(blank=True, null=True)
    labels_it = models.JSONField(blank=True, null=True)

    short_description = models.TextField()
    short_description_it = models.TextField()

    description = models.TextField()
    description_it = models.TextField()

    rating = models.FloatField()

    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    revenue = models.IntegerField(default=0)
    purchased = models.IntegerField(default=0)

    affiliate_link = models.URLField(blank=True, null=True)

    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    categories = models.ManyToManyField(Category, blank=True, related_name="products")

    see_also = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(
        upload_to="products/images/%Y/%m/%d", blank=True, null=True
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField()
    feedback = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}({self.user.email}) {self.product.name}"
