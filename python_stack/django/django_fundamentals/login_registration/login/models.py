from django.db import models


class loginManager(models.Manager):
    def basic_validator(self,post_data):
        errors={}

        if len(post_data['email'])<2:
            errors['email'] = "email must be at least 2 charectars"
        
        if len(post_data['password'])<3:
            errors['password'] = "password must be at least 3 charectars"
        
        if len(post_data['name'])<2:
            errors['name'] = "name must be at least 2 charectars"
        
        return errors



class Users(models.Model):

    
    email = models.CharField(max_length=255,default="")
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = loginManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def register (email , username , password):
    Users.objects.create(email=email , password = password , name=username)

def check_user (email,password):
    
    user = Users.objects.filter(email=email)
    print(user)
    if user == None :
        return False
    
    if user[0].password==password:
        return True
    return False
    
# Create your models here.
