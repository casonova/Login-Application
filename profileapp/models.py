from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(default="John Doe", max_length=200, null=True)
    phone_number = models.CharField(max_length=20,validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.'
            ), 
        ], null=True
        )
    address = models.TextField(default="Iqbal Town", max_length=200, null=True)
    profile_img = models.ImageField(default='images/default.jpg', upload_to="images", null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
 