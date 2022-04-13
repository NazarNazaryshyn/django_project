from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=40, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)


    def __str__(self):
        return f'{self.name} {self.position}'

    class Meta:
        ordering = ('position',)

class Dish(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes', filename)

    name = models.CharField(max_length=30, unique=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    position = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}: {self.price}'

    def get_absolute_url(self):
        return reverse('get_dish_page', kwargs={'post_id': self.id})


class Advantage(models.Model):
    name = models.CharField(max_length=60, db_index=True, unique=True)
    description = models.TextField(max_length=700, blank=True)

class Chef(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{self.first_name}.{ext}'
        return path.join('images/chefs', filename)



    first_name = models.CharField(max_length=50, unique=True, db_index=True)
    second_name = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.CharField(max_length=50, unique=True, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    instagram_link = models.CharField(max_length=150,db_index=True, unique=True)
    facebook_link = models.CharField(max_length=150,db_index=True, unique=True)
    twitter_link = models.CharField(max_length=150,db_index=True, unique=True)
    linkedin_link = models.CharField(max_length=150,db_index=True, unique=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL', null=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    def get_absolute_url(self):
        return reverse('chef_view', kwargs={'post_slug': self.slug})

class Gallery(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'photo_{self.id}.{ext}'
        return path.join('images/gallery', filename)

    image = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

class Slide(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'slide_photo{self.id}.{ext}'
        return path.join('image/slides', filename)

    image = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

class Customer(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'photo_{self.second_name}.{ext}'
        return path.join('images/customers', filename)
    
    first_name = models.CharField(max_length=50, db_index=True)
    second_name = models.CharField(max_length=50, db_index=True)
    position = models.CharField(max_length=50, db_index=True)
    stars = models.IntegerField()
    comment = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

class Photo(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'photo_{self.name}.{ext}'
        return path.join('images/photos', filename)

    name = models.CharField(max_length=50, db_index=True, unique=True)
    is_visible = models.BooleanField(default=True)
    image = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}'

class UserReservation(models.Model):
    mobile_regex = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')
    phone = models.CharField(max_length=35, validators=[mobile_regex])
    name = models.CharField(max_length=50, unique=True, db_index=True)
    persons = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=500, blank=True)
    is_processed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date',)


    def __str__(self):
        return f'{self.name}, {self.phone}: {self.message[:30]} '


class UserContacts(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True)
    message = models.TextField(max_length=500, blank=True)
    subject = models.CharField(max_length=50, blank=True, db_index=True)
    is_processed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    class Meta:
        ordering = ('date',)


    def __str__(self):
        return f'{self.name}, {self.email}: {self.message}'


