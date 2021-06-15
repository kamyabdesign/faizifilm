from django.db import models
from django.urls import reverse
from django.utils import timezone
from extensions.utils import jalali_converter
from blog.models import Author, Category


class Work (models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ManyToManyField(Category, related_name="work")
    photo_work = models.ImageField(upload_to="work", verbose_name='تصاویر')
    video = models.URLField(max_length=300)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('work_detail', kwargs={
            'slug': self.slug
        })

    def jpublish(self):
        return jalali_converter(self.publish)

    def delete(self, *args, **kwargs):
        self.photo_work.delete()
        super().delete(*args, **kwargs)


class Item(models.Model):
    address = models.TextField(blank=True)
    about = models.TextField(blank=True)
    phone = models.IntegerField()
    email = models.EmailField()
    logo = models.ImageField(upload_to="logo")
    twitter = models.URLField()
    facebook = models.URLField()
    telegram = models.URLField()
    instagram = models.URLField()
    social_img1 = models.ImageField(upload_to="social")
    social_img2 = models.ImageField(upload_to="social")
    social_img3 = models.ImageField(upload_to="social")
    social_img4 = models.ImageField(upload_to="social")
    social_img5 = models.ImageField(upload_to="social")
    social_img6 = models.ImageField(upload_to="social")

    def __str__(self):
        return self.address

    def delete(self, *args, **kwargs):
        self.social_img1.delete()
        self.social_img2.delete()
        self.social_img3.delete()
        self.social_img4.delete()
        self.social_img5.delete()
        self.social_img6.delete()
        self.logo.delete()
        super().delete(*args, **kwargs)
