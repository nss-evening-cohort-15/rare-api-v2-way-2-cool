from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# class name should be PascalCase
class RareUser(models.Model):
  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    # auto_now_add: first created timestamp; 
    # auto_add: overwrite when everytime it's saved
    active = models.BooleanField(default=True)
    profile_image_url = models.URLField() #default max_length=200
    subscription = models.ManyToManyField('rareapi.RareUser', related_name='subscribe_by') # attendees
    
    
    # for custom properties that are not stored in the database
    @property
    def subscribed(self):
        return self.__subscribed
    
    @subscribed.setter
    def subscribed(self, value):
        self.__subscribed = value