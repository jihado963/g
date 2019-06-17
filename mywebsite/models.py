from django.db import models
# Create your models here.
class personM(models.Model):

    email = models.EmailField(max_length=64)
    f_name = models.CharField(max_length=32)
    l_name = models.CharField(max_length=32)
    phone_num = models.TextField()
     
    def __str__(self):
        return self.f_name