import datetime

from django.db import models
from django.urls import reverse


# Create your models here.
class Media_models(models.Model):

    type_f = [
        ('img', 'img'),
        ('video','video'),
        ('none','none')
    ]

    title = models.CharField('Title',max_length=255,blank=True)
    media_video = models.FileField('Media_video',upload_to='video/%Y/%m/%d/',blank=True)
    media_img = models.ImageField('Media_img', upload_to='img/%Y/%m/%d/',blank=True)
    post = models.TextField('Post',blank=True)
    data_time_create = models.DateTimeField(auto_now_add=True)
    data_time_update = models.DateTimeField(auto_now=True)
    type_file = models.CharField('File_type',max_length=100,choices=type_f,blank=True)
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name='URL')

    def get_urls(self):
        return reverse('post',kwargs={'post_slug':self.slug})

    class Meta:
        verbose_name = 'Media content'
        # verbose_name_plural = 'Media content'
        ordering = ['-data_time_update','title']