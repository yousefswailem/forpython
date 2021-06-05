from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self,post_data):
        errors={}

        if len(post_data['title'])<2:
            errors['title'] = "title must be at least 2 charectars"
        
        if len(post_data['network'])<3:
            errors['network'] = "network must be at least 3 charectars"
        
        if len(post_data['desc'])<10:
            errors['desc'] = "description must be at least 10 charectars"
        
        return errors




class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField(default="")
    created_at = models.DateTimeField (auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

