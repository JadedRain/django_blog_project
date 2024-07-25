from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import UserRegistationForm, UserUpdateFrom, ProfileUpdateForm
import os


def register_view(request):
    if request.method == 'POST':
        form = UserRegistationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You can now log in!')
            return redirect('blog-index')
    else:
        form = UserRegistationForm()
    return render(request, 'users_app/register.html', {'title':'Register', 
                                                       'form': form})

def user_logout_view(request):
    logout(request)
    return render(request, 'users_app/logout.html')

@login_required
def profile(request):
    if request.method == 'POST':
        if request.user.profile.image.url != '/media/default.jpg':
            os.remove(os.path.join(settings.MEDIA_ROOT, request.user.profile.image.name))
        user_update_form = UserUpdateFrom(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, 
                                                request.FILES, 
                                                instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        user_update_form = UserUpdateFrom(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    
    return render(request, 'users_app/profile.html', context)