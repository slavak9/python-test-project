from main.model_forms import filter_mod
from .models import Media_models


img_list = ['.jpg', '.jpeg', '.JPE', '.jpe', '.jp2', '.bmp', '.bmp2', '.bmp3', '.gif', '.png', '.png8', '.png24',
            '.png32', '.tiff', '.tif', '.ptif', '.tiff64', '.psd', '.xcf', '.ico', '.icon', '.svg', '.svgz', '.msvgz',
            '.eps', '.eps2', '.eps3', '.epsf', '.ai', '.nef', '.cr2', '.crw', '.dcr', '.kdc', '.k25', '.x3f', '.arw',
            '.sr2', '.srf', '.mrw', '.erf', '.raf', '.pct', '.pict', '.dds', '.dng', '.pex', '.3fr', '.ppm', '.orf',
            '.pef', '.aai', '.exr', '.hdr', '.dcm', '.dicom', '.psb', '.pbm', '.jpf', '.iff', '.sct', '.tga', '.fit',
            '.fits', '.fts', '.mng', '.pgm', '.pnm', '.pam', '.ps', '.ps2', '.ps3', '.sgi', '.xpm', '.xbm', '.bitmap',
            '.xwd', '.pcx', '.pcc', '.cur']

video_list = ['.mp4', '.mov', '.m4v', '.m2v', '.avi', '.wmv', '.rm', '.mpeg', '.mpg', '.ogv', '.3gp', '.3g2', '.vob',
              '.flv', '.webm', '.mkv']


def img(value):
    str_value = str(value).lower()
    for i in img_list:
        if i.lower() in str_value and str_value[len(str_value) - len(i):] == i:
            return True
    return False


def video(value):
    video_list = ['.mp4', '.mov', '.m4v', '.m2v', '.avi', '.wmv', '.rm', '.mpeg', '.mpg', '.ogv', '.3gp', '.3g2',
                  '.vob', '.flv', '.webm', '.mkv']
    str_value = str(value).lower()
    for i in video_list:
        if i in str_value and str_value[len(str_value) - len(i):] == i:
            return True
    return False

def control_slug(data:str):
    sibol = ['!','"','£','$','%','&','/','(',')','=','?','^','*','°',':',';',"'",'+','.',' ']
    for i in sibol:
        if i in data:
            data = data.replace(i,'_')
    return data


def get_post(data: dict):
    model = Media_models()
    dis_error = ('green', "Content was successfully saved")
    for key, value in data.items():
        if key == 'title':
            if len(value) > 60:
                return ('orange', f"60 simbols is aloud for field 'Title'. You have enterd {len(value)} simbols")
            elif filter_mod(value):
                return ('orange',f"The title with name ({value}) olready exsist")
            else:
                model.title = value
                clean_slug = control_slug(value)
                model.slug = clean_slug
        elif key == 'post':
            model.post = value

        elif key == 'media_file':
            if value == None:
                model.type_file = 'none'
                model.save()
                return dis_error

            elif img(value):
                model.type_file = 'img'
                model.media_img = value
                model.save()
                return dis_error

            elif video(value):
                model.type_file = 'video'
                model.media_video = value
                model.save()
                return dis_error
            else:
                return (
                    'orange',
                    f"The file ({value}) can't be supported. \nPlease try again. \n It's should be Image or Video")
