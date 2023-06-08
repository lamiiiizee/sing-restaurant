from django.db import models
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField
from django.core.validators import MinLengthValidator
# Create your models here.


class Menu(models.Model):
    ClassName_CHOICES = (
        ('starters', 'starters'),
        ('main-dishes', 'main-dishes'),
        ('drinks', 'drinks'),
        ('desserts', 'desserts'),
        ('icecream', 'icecream'),
    )
    image = VersatileImageField(upload_to = "Menus")
    name = models.CharField(max_length=100,blank=True,null=True)
    # price = models.IntegerField(blank=True,null=True)
    # ClassName = models.CharField(max_length=50,blank=True,null=True)
    ClassName= models.CharField(max_length=50,choices=ClassName_CHOICES,verbose_name="category")



    def __str__(self):
        return self.name



class Branch(models.Model):
    image = VersatileImageField(upload_to = "img_branches")
    name = models.CharField(max_length=20,blank=True,null=True,verbose_name="Branch Name")
    branch_contact_number_1 = models.CharField(max_length=20,blank=True, null=True, verbose_name="Branch number")
    branch_contact_number_2 = models.CharField(max_length=20, blank=True,null=True, verbose_name="Branch number")
    location = models.CharField(max_length=100,blank=True,null=True,verbose_name="Branch location")


    class Meta:
        verbose_name = "Add your branch"
        verbose_name_plural = "Add your branches"
        
    def __str__(self):
        return self.name


class Review(models.Model):
    massage = models.CharField(max_length=60,blank=True,null=True)
    review = HTMLField(max_length=300,blank=True,null=True)
    Guest = VersatileImageField(upload_to = "review_guest")
    Guest_name = models.CharField(max_length=20,blank=True,null=True,verbose_name="Guest Name")


    def __str__(self):
        return self.Guest_name
    
    


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)
    
    

class Gallery(models.Model):
    image = VersatileImageField(upload_to = "gallery")

    class Meta:
       verbose_name = "Add gallery"
       verbose_name_plural = "Add galleries"





class CarouselSlide(models.Model):
    image = VersatileImageField(upload_to = "CarouselSlide")
    prev_slide = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='next_slides')


    class Meta:
       verbose_name = "Home Slide image"
       verbose_name_plural = "Home Slide images"
    name = 'home slider image'

    def __str__(self):
        return str(self.name)