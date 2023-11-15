from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Profile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=20, 
        validators=[RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.'
            )],
        null=True
    )
    address = models.TextField(max_length=200, null=True,blank=True)
    profile_img = models.ImageField(default='images/default.jpg', upload_to="images", null=True, blank=True)
    
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"
        
    def __str__(self):
        return f"{self.user.username}'s profile"
    
 