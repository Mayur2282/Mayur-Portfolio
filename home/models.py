from django.db import models
# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    date = models.DateTimeField()
    
    
    def __str__(self):
        return self.name
    

    

    


