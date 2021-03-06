from django.db import models
from django.urls import reverse # new 

# Create your models here.
# books/models.py

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    # def get_absolute_url(self): # new
    #     return reverse('book_detail', args=[str(self.id)])

# class Instagram_info(models.Model):
#     instagram_ID = models.CharField(max_length=200)
#     Email = models.CharField(max_length=200)


    # def __str__(self):
    #     return self.title