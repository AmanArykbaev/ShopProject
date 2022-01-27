from django.db import models


# Create your models here.
class Clothes(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Number')
    cloth_name = models.CharField(max_length=200, verbose_name='Title')
    cloth_brand = models.CharField(max_length=200, verbose_name='Brand Name')
    cloth_size = models.CharField(max_length=200, verbose_name='Size')
    cloth_date_release = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Category')
    is_published = models.BooleanField(default=True, verbose_name='Published')

    def __str__(self):
        return self.cloth_name

    class Meta:
        verbose_name = 'Clothes'
        verbose_name_plural = 'Clothes'
        ordering = ['cloth_date_release']


class Category(models.Model):
    cloth_name = models.CharField(max_length=150, db_index=True, verbose_name="Category")

    def __str__(self):
        return self.cloth_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['cloth_name']
