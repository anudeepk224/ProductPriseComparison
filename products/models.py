from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(default='default-product.png', blank=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('products:filtered_products', args=[self.slug])



    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    url_amazon = models.CharField(max_length=250, db_index=True)
    url_flipkart = models.CharField(max_length=250, db_index=True)
    url_bigbasket = models.CharField(max_length=250, db_index=True)

    price_amazon = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_flipkart = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_bigbasket = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(default='default-product.png', blank=True, upload_to='product-thumbnails')
    # make all thumbnails at most 140x140pixels
    class Meta:
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
