from django.db import models
import datetime
from add_content.models import Media_models

# Create your models here.
class Comments(models.Model):
    name = models.CharField('Name',max_length=50)
    comment = models.TextField()
    data_time = models.DateTimeField(auto_now_add=True,blank=True)
    user_comment = models.ForeignKey(Media_models,on_delete=models.CASCADE,default=None,verbose_name='Model_ID')
    slug = models.SlugField(max_length=255,db_index=True, verbose_name='Association')




    class Meta:
        verbose_name = 'Comment'
        # verbose_name_plural = 'Comment'
        ordering = ['-data_time', 'name']

