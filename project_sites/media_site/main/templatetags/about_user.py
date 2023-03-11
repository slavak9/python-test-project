from django import template
from user_profile.models import *
from user_profile.edit import about
register = template.Library()
@register.simple_tag()
def get_contacts():
    return about()

