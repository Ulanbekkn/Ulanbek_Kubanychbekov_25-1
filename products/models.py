from django.db import models


class Hashtag(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Products(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    phone_status = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    hashtags = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=255)
    rate = models.IntegerField()
    created_date = models.DateField(auto_now_add=True, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

