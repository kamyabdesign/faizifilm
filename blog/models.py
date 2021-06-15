from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from extensions.utils import jalali_converter


class Author (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='author')

    def __str__(self):
        return str(self.user)

    def delete(self, *args, **kwargs):
        self.profile_pic.delete()
        super().delete(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    published_at = models.DateTimeField(
        auto_now=False, auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Tag (models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    create_at = models.DateTimeField(
        auto_now=False, auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Article (models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'published'),
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="blog", null=True, blank=True)
    tag = models.ManyToManyField("Tag", related_name="blogs")
    image = models.ImageField(upload_to="post")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={
            'slug': self.slug
        })

    def jpublish(self):
        return jalali_converter(self.publish)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class Comments(models.Model):
    blog = models.ForeignKey("Article", verbose_name=_(
        "مقالات"), related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربری"), max_length=50)
    email = models.EmailField(_("آدرس الکترونیکی"), max_length=254)
    message = models.TextField(_("متن پیام"))
    image = models.ImageField(
        _("تصویر"), upload_to='comments', default='default/avatar.jpg')
    date = models.DateTimeField(
        _("تاریخ انتشار"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def jpublish(self):
        return jalali_converter(self.date)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class Alls(models.Model):
    name = models.CharField(_("عنوان"), max_length=150)
    phone = models.CharField(_("شماره تماس"), max_length=50)
    email = models.EmailField(_("ایمل"), max_length=254)
    address = models.TextField(_("آدرس شرکت"))
    social_face = models.URLField(
        _("فیسبوک"), max_length=250, blank=True, null=True)
    social_twitter = models.URLField(
        _("تویتتر"), max_length=250, blank=True, null=True)
    social_telegram = models.URLField(
        _("تلگرام"), max_length=250, blank=True, null=True)
    social_inestagram = models.URLField(
        _("انیستاگرام"), max_length=250, blank=True, null=True)
    logo = models.ImageField(_("لوگو"), upload_to="logo")
    about_us = models.TextField(_("درمورد ما"))
    map_area = models.URLField(_("گوگل مپ"), max_length=300, blank=True)
    timestamp = models.DateField(default=timezone.now)
    face_pic1 = models.ImageField(_("1تصویر فیسبوک"), upload_to="face_pic")
    face_pic2 = models.ImageField(_("2تصویر فیسبوک"), upload_to="face_pic")
    face_pic3 = models.ImageField(_("3تصویر فیسبوک"), upload_to="face_pic")
    face_pic4 = models.ImageField(_("4تصویر فیسبوک"), upload_to="face_pic")
    face_pic5 = models.ImageField(_("5تصویر فیسبوک"), upload_to="face_pic")
    face_pic6 = models.ImageField(_("6تصویر فیسبوک"), upload_to="face_pic")

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.logo.delete()
        self.face_pic1.delete()
        self.face_pic2.delete()
        self.face_pic3.delete()
        self.face_pic4.delete()
        self.face_pic5.delete()
        self.face_pic6.delete()
        super().delete(*args, **kwargs)
