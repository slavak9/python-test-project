from django.contrib import admin
from add_content.models import Media_models
from main.models import Comments
from user_profile.models import Usermodel

# Register your models here.
class Amin_media(admin.ModelAdmin):
    list_display = ('id','title','post','media_video','media_img','data_time_update','type_file')
    search_fields = ('title','post')
    list_filter = ('data_time_create','data_time_update')
    prepopulated_fields = {'slug':('title',)}

class Amin_comment(admin.ModelAdmin):
    list_display = ('id','name','comment','data_time','user_comment','slug')
    search_fields = ('name',)
    list_filter = ('data_time',)

class Amin_user(admin.ModelAdmin):
    list_display = ('id','name','last_name','city','photo')



admin.site.register(Media_models,Amin_media)
admin.site.register(Comments,Amin_comment)
admin.site.register(Usermodel,Amin_user)