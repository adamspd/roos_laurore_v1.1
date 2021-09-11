from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
from django.views.generic import ListView

from .form import CustomRegisterForm
from client.models import Photo


def register_page(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('client:login')
    else:
        form = CustomRegisterForm()
    context = {'form': form}
    return render(request, 'client/register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("user is logged in ")
            # Redirect to a success page.
            return redirect('client:client_homepage')
        else:
            # Return an 'invalid login' error message.
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'client/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('client:login')


@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        username = request.user.pk
        all_photos = Photo.objects.filter(owner_id=username)
        context = {'all_photos': all_photos}
        return render(request, 'client/index.html', context)
    else:
        return render(request, 'client/login.html')


@login_required(login_url='login')
def favorite(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    try:
        selected_photo = photo.objects.get(pk=request.POST['photo'])
    except (KeyError, Photo.DoesNotExist):
        return render(request, 'client/index.html', {
            'photo': photo,
            'error_message': "You didn't like a photo",
        })
    else:
        selected_photo.is_favorite = True
        selected_photo.save()
        return render(request, 'client/index.html', {
            'photo': photo,
        })

