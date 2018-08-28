from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SlamBook(models.Model):
    being_written_to = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    my_name = models.CharField(max_length=250,default='')
    my_nickname = models.CharField(max_length=250,default='')
    my_address = models.CharField(max_length=250,default='')
    my_mobile_number = models.CharField(max_length=250,default='')
    my_email = models.EmailField(max_length=250,default='')
    my_birth_day = models.CharField(max_length=250,default='')
    my_zodiac_sign = models.CharField(max_length=250,default='')
    my_crushes = models.CharField(max_length=250,default='')
    my_happiest_moment = models.CharField(max_length=250,default='')
    my_favourite_dishes = models.CharField(max_length=250,default='')
    my_favourite_sports = models.CharField(max_length=250,default='')
    my_favourite_places = models.CharField(max_length=250,default='')
    my_favourite_actor = models.CharField(max_length=250,default='')
    my_favourite_actress = models.CharField(max_length=250,default='')
    my_favourite_webiste = models.CharField(max_length=250,default='')
    my_favourite_festival = models.CharField(max_length=250,default='')
    my_favourite_song = models.CharField(max_length=250,default='')
    my_ideal = models.CharField(max_length=250,default='')
    opinion_about_you = models.CharField(max_length=250,default='')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.my_name