from django.db import models

# Create your models here.

class Usermodel(models.Model):

    name = models.CharField('Name',max_length=50)
    last_name = models.CharField('Last_name',max_length=50)
    city = models.CharField('City',max_length=50)
    photo = models.ImageField('Foto_avatar',upload_to='img/avatar',blank=True)
    data_time_create = models.DateTimeField(auto_now_add=True)
    data_time_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User personal profile'
        # verbose_name_plural = 'Comment'
        ordering = ['name',]