from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistationForm

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
    return render(request, 'users_app/profile.html')