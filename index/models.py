from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return str(self.name)

class Area(models.Model):
    name = models.CharField(max_length=10)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    name = models.CharField(max_length=10)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.name)


