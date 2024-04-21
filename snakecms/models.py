from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    person_text = models.TextField() 
    head_color = models.CharField(max_length=7)  
    project_text = models.TextField() 
    body_color = models.CharField(max_length=7)  
    footer_color = models.CharField(max_length=7)  
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    user_photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)  
    website_photo = models.ImageField(upload_to='website_photos/', blank=True, null=True)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
