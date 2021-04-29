from django.db import models
from django.contrib import admin
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="imgdb/")
    video = models.FileField(upload_to="video/")
    
         

class AdminLogin(models.Model):
    uname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
  

class Movie(models.Model):
    movieId = models.CharField(max_length=9)
    title = models.CharField(max_length=180)
    genres = models.CharField(max_length=90)
    imdbId = models.CharField(max_length=10)
    average = models.CharField(max_length=6)
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to="imgdb/",null=True)
    video = models.FileField(upload_to="video/",null=True)


class Review(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=500)

class Check(models.Model):
    image = models.ImageField(upload_to="check/")