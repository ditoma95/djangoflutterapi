from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name + " " + str(self.date_added)

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, related_name = 'Categorie', on_delete=models.CASCADE)
    image = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title + "" + str(self.price) + " " + self.description + " " + str(self.category) + " " + str(self.date_added)