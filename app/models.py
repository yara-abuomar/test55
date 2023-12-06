from django.db import models
from datetime import date

class showManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['title1'])<2:
            errors['title1']="title should be atleast 2 char"
        if len(postData['title1'])<1:
            errors['title1']="title should added mandatory"
        if len(postData['net'])<3:
            errors['net']="net should be atleast 3 char"
        if len(postData['net'])<1:
            errors['net']="net should added mandatory"
        if len(postData['desc1'])<10:
            errors['desc1']="desc  shouldbe at least 10 char"
        if len(postData['rele'])<1:
            errors['rele']="date  shouldbe added"
        if len(Show.objects.filter(title=postData['title1']))>0:
            errors['title1']="title should be uniqe"
        return errors
        

class Show(models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    release_date=models.DateTimeField(("Date"),default=date.today)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=showManager()



   


    


# Create your models here.
