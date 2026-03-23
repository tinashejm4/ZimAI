from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user           = models.OneToOneField(User, on_delete = models.CASCADE)
    slug           = models.SlugField(max_length=250, null =True, blank =True, editable=False)
    bio            = models.CharField(max_length=1000, default='')
    date_joined    = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save()

class ProfileImage(models.Model):
    user           = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_image  = models.ImageField(default = 'profile_pics/profile_default.png', upload_to='profile_pics')