from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from add_content.models import Media_models
from main.model_forms import filter_com
from main.forms_main import Comments_form, RegisterForm, Login_form

def main(request):
    data = Media_models.objects.order_by('-data_time_update')
    return render(request, 'main/main_page.html', {'data': data})


def post(request, post_slug):
    error = False
    form_comment = Comments_form()
    post = get_object_or_404(Media_models, slug=post_slug)
    comment = filter_com(post_slug)
    if request.method == 'POST':
        if request.user.is_authenticated:
            print('user ok')
            form_comment = Comments_form(request.POST)
            if form_comment.is_valid():
                form = form_comment.save(commit=False)
                form.user_comment = Media_models(post.id)
                form.slug = post_slug
                form.name = request.user.username
                form.save()
                return redirect(f'/post/{post_slug}')
        else:
            error = True
            print(error)

    else:
        form_comment = Comments_form()
    return render(request, 'main/post.html', {'post': post, 'comments': comment, 'form': form_comment,'error':error})


def register(request):
    global form_reg
    error = ''
    if request.method == 'POST':
        if request.user.is_authenticated:
            error = "you can't register again"
        else:
            form_reg = RegisterForm(request.POST)
            if form_reg.is_valid():
                user = form_reg.save(commit=False)
                user.is_staff = True
                user.save()
                g = Group.objects.get(name='view_add_comment')
                user.groups.add(g)
                return redirect('main')
            else:
                error = 'The password is too bad or not valid'
    else:
        form_reg = RegisterForm()
    return render(request, 'main/register.html', {'register': form_reg, 'error': error})

def login_user(request):
    global met
    error = ''
    form_login = Login_form()
    if request.method == 'GET':
        met = request.GET['next']
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(met)

        else:
            error = 'Username or Password are wrong'

    return render(request,'main/login.html',{'login':form_login,'error':error})

def logout_user(request):
    logout(request)
    return redirect('main')


def pageNotFound(reguest,exception):
    return render(reguest,'main/page_not_found.html')