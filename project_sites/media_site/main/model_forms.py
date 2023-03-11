from add_content.models import Media_models
from main.models import Comments

# filter add_content models
def filter_mod(data):
    try:
        return Media_models.objects.filter(slug=data)
    except Exception:
        return False

def get_mod(data):
    try:
        return Media_models.objects.get(slug=data)
    except Exception:
        return False


# filter main comments
def filter_com(data):
    try:
        return Comments.objects.filter(slug=data)
    except Exception:
        return False

def filter_title(data):
    try:
        return Media_models.objects.get(title=data)
    except Exception:
        return False

def get_com(data):
    try:
        return Comments.objects.get(slug=data)
    except Exception:
        return False