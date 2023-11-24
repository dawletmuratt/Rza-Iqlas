from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(max_length=100, null=True, blank=True)
    san = models.IntegerField()
    images = models.ImageField()
class Category(models.Model):
    name = models.CharField(max_length=45, verbose_name='Category name')
    slug = models.SlugField(max_length=125)
    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return f'{self.slug}'
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=45)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=4)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)