from add_content.post_control import img, video, control_slug
from main.model_forms import filter_com, filter_mod, filter_title, get_mod
from user_profile.models import Usermodel

b = ('back',)
EDIT = []
count = 0

def about():
    try:
        return Usermodel.objects.get(id=1)
    except Exception:
        return False

def value():
    return get_mod(EDIT[0])


def delete(data: dict):
    global EDIT
    if 'delete_value' in data:
        slug = data['delete_value']
        value = filter_mod(slug)
        value.delete()
    elif 'edit content' in data:
        if EDIT:
            EDIT.clear()
            EDIT.append(data['edit content'])
            return True
        else:
            EDIT.append(data['edit content'])
            return True


def edit_slug(data):
    comment = filter_com(EDIT[0])
    for i in comment:
        i.slug = data
        i.save()


def is_title(data):
    try:
        return filter_title(data)
    except Exception:
        return False


def edit_data(data):
    global count
    if EDIT:
        model = get_mod(EDIT[0])
        dis_error = ('green', "Content was successfully saved")
        for key, value in data.items():
            if key == 'title':
                g = is_title(value)
                clean_slug = control_slug(value)
                if len(value) > 60:
                    return ('orange', f"60 simbols is aloud for field 'Title'. You have enterd {len(value)} simbols")
                else:
                    if g:
                        if g.title == value and g.id != model.id:
                            return ('orange', f"The title with name ({value}) olready exsist")
                        elif g.title == value and g.id == model.id:
                            model.title = value
                            model.slug = clean_slug
                    else:
                        model.title = value
                        model.slug = clean_slug
            elif key == 'post':
                model.post = value

            elif key == 'media_file':
                if value == None:
                    model.media_img = ''
                    model.media_video = ''
                    model.type_file = 'none'
                    edit_slug(clean_slug)
                    model.save()
                    EDIT.clear()
                    return dis_error

                elif img(value):
                    model.type_file = 'img'
                    model.media_img = value
                    edit_slug(clean_slug)
                    model.save()
                    EDIT.clear()
                    return dis_error

                elif video(value):
                    model.type_file = 'video'
                    model.media_video = value
                    edit_slug(clean_slug)
                    model.save()
                    EDIT.clear()
                    return dis_error
                else:
                    return (
                        'orange',
                        f"The file ({value}) can't be supported. \nPlease try again. \n It's should be Image or Video")
    else:
        return b

def delet():
    obj = Usermodel.objects.all()
    num = 0
    if obj:
        for i in obj:
            if num < i.id:
                num = i.id
        obg_clean = Usermodel.objects.get(id=num)
        obg_clean.id = 1
        for g in obj:
            if g.id != 1:
                g.delete()

def user_per_data(form_data:dict):
    try:
        form = Usermodel.objects.get(id=1)
    except Exception:
        form = Usermodel()
    for key,value in form_data.items():
        if key == 'name':
            form.name = value
        elif key == 'last_name':
            form.last_name = value
        elif key == 'city':
            form.city = value
        elif key == 'photo':
            if value != None:
                form.photo = value
                form.save()
            else:
                form.save()