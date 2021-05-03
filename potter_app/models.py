from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)


class Category(models.Model):
    cat_name = models.CharField(verbose_name="Category Name", max_length=50)
    cat_desc = models.TextField(verbose_name="Category Description")

    def __str__(self):
        return self.cat_name

class Gallery(models.Model):
    name = models.CharField(max_length=50, default="")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default="")
    gallery_img = models.ImageField(verbose_name= "Image", upload_to='uploads/gallery', default="")
    date_created = models.DateTimeField(verbose_name="Date Created", default=timezone.now)

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='uploads/events')
    date_created = models.DateField(
        verbose_name="Date Created", default=timezone.now)
    time_created = models.TimeField(
        verbose_name="Time Created", default=timezone.now)

    def __str__(self):
        return self.name
