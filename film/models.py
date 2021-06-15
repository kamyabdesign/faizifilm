from django.db import models
from django.utils.translation import gettext as _


class Main (models.Model):
    title = models.CharField(max_length=200)
    overview = models.CharField(max_length=250)
    images = models.ImageField(upload_to="main", blank=True, null=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.images.delete()
        super().delete(*args, **kwargs)


class Hestory(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    yeras = models.IntegerField(blank=True)
    picture = models.ImageField(upload_to="hestory")
    data_date = models.DateField(blank=True, null=True)
    work_title = models.CharField(max_length=150)
    work_detail = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)


class Team (models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=250)
    team_pic = models.ImageField(upload_to="team_pic")
    tiwitter = models.URLField(max_length=150, blank=True)
    facebook = models.URLField(max_length=150, blank=True)
    instagram = models.URLField(max_length=150, blank=True)
    telegram = models.URLField(max_length=150, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.team_pic.delete()
        super().delete(*args, **kwargs)


class Video (models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=150)
    link = models.URLField(blank=True)
    img = models.ImageField(upload_to="video", null=True, default=True)
    create = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)


class Trust(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    image_1 = models.ImageField(upload_to="trust")
    image_2 = models.ImageField(upload_to="trust")
    image_3 = models.ImageField(upload_to="trust")
    image_4 = models.ImageField(upload_to="trust")

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image_1.delete()
        self.image_2.delete()
        self.image_3.delete()
        self.image_4.delete()
        super().delete(*args, **kwargs)


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name


class our_service(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Features (models.Model):
    name = models.CharField(max_length=150)
    detail = models.TextField(blank=True)
    img = models.ImageField(upload_to="feature")

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.img.delete()
        super().delete(*args, **kwargs)
