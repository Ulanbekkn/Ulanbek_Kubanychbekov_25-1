from django.db import models

class Products(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    phone_status = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
