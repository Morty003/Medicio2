from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator

class Doctors(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().strip('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/doctors', filename)

    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)
    desc = models.TextField(max_length=500, blank=True)
    post = models.CharField(max_length=50, unique=False)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.name}: {self.position}'

class Meta:
    ordering = ('position', )

class Services(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)
    desc = models.TextField(max_length=500, blank=True)


class UserReservation(models.Model):
    mobile_regex = RegexValidator(regex='/^(\+\d{1,3}[- ]?)?\d{10}$/', message='Phone format in +380501234567')
    name = models.CharField(max_length=50, unique=True, db_index=True)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=15, validators=[mobile_regex])
    message = models.TextField(max_length=500, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', )


    def __str__(self):
        return f'{self.name}, {self.phone}: {self.message[:30]}'

# class Pricing(models.Model):
#     name = models.CharField(max_length=50, unique=True, db_index=True)
#     options_1 = models.CharField(max_length=50, unique=False)
#     options_2 = models.CharField(max_length=50, unique=False)
#     options_3 = models.CharField(max_length=50, unique=False)
#     options_4 = models.CharField(max_length=50, unique=False)
#     options_5 = models.CharField(max_length=50, unique=False)
#     price = models.IntegerField()

class Departaments(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().strip('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/departments', filename)
    name = models.CharField(max_length=50, unique=True, db_index=True)
    small_desc = models.TextField(max_length=100, blank=True)
    desc = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField(unique=True)


