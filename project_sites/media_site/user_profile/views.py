from django.contrib.auth.decorators import permission_required
from django.shortcuts import render,redirect
from django.http import HttpResponse

from add_content.forms import Add_Models_forms_manualy
from add_content.models import Media_models
from add_content.post_control import get_post
from user_profile.edit import delete, edit_data, value, user_per_data, about
from user_profile.forms import User_form
from user_profile.models import Usermodel


# Create your views here.

def user_profile(request):
    if request.user.has_perm('add_content.add_media_models'):
        data = Media_models.objects.order_by('-data_time_update')
        if request.user.has_perm('user_profile.add_media_models'):
            if request.method == 'POST':
                anser = delete(request.POST)
                if anser:
                    return redirect('edit')
        return render(request, 'user_profile/my_profile.html',{'data':data})
    else:
        return render(request, 'add_content/restrictions.html')

def user_personal_data(request):
    if request.user.has_perm('user_profile.add_usermode'):
        if request.method == 'POST':
            user_form = User_form(request.POST,request.FILES)
            if user_form.is_valid():
                user_per_data(user_form.cleaned_data)
        else:
            form = about()
            if form:
                user_form = User_form(initial={'name': form.name, 'last_name': form.last_name, 'city': form.city})
            else:
                user_form = User_form()
        return render(request,'user_profile/edit_profile.html',{'user':user_form})
    else:
        return render(request, 'add_content/restrictions.html')


def edit(request):
    if request.user.has_perm('add_content.add_media_models'):
        colection = {}
        if request.method == 'POST':
            form = Add_Models_forms_manualy(request.POST,request.FILES)
            if form.is_valid():
                answear = edit_data(form.cleaned_data)
                if answear:
                    if answear[0] == 'back':
                       return redirect('user_profile')
                    elif answear[0] == 'green':
                        colection['green'] = answear[1]
                    elif answear[0] == 'orange':
                        colection['orange'] = answear[1]
        else:
            val = value()
            form = Add_Models_forms_manualy(initial={'title':val.title,'post':val.post})
        colection['form'] = form
        return render(request, 'user_profile/edit_content.html',colection)
    else:
        return render(request, 'add_content/restrictions.html')