from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Thread(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    image = models.ImageField(upload_to="uploads/", height_field=None, width_field=None, max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class ThreadResponse(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    response = models.TextField()
    created = models.DateTimeField(auto_now_add=True)