from django.shortcuts import render,redirect
from add_content.forms import Add_Models_forms_manualy
from .post_control import get_post


def add_content(request):
    if request.user.has_perm('add_content.add_media_models'):
        colection = {}
        if request.method == 'POST':
            form = Add_Models_forms_manualy(request.POST,request.FILES)
            if form.is_valid():
                answear = get_post(form.cleaned_data)
                if answear:
                    if answear[0] == 'green':
                        colection['green'] = answear[1]
                    elif answear[0] == 'orange':
                        colection['orange'] = answear[1]

        else:
            form = Add_Models_forms_manualy()
        colection['form'] = form
        return render(request, 'add_content/add_content.html',colection)
    else:
        return render(request, 'add_content/restrictions.html')




