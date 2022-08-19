from django.db import models

# Create your models here.
class Products(models.Model):

    def __str__(self):
        return self.name

    name=models.CharField(max_length=200)
    price=models.FloatField()
    discount=models.FloatField()
    category=models.CharField(max_length=200)
    description=models.TextField()
    image=models.CharField(max_length=500)
