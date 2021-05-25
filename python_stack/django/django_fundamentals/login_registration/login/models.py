from django.db import models



class Users(models.Model):

    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def register (name, passwd):
    Users.objects.create(name = name,password = passwd)

def check_user (name,passwd):
    
    user = Users.objects.filter(name=name)
    print(user)
    if user == None :
        return False
    
    if user[0].password==passwd:
        return True
    return False
    
# Create your models here.
