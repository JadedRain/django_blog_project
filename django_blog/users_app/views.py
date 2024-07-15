from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistationForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created: {username}!')
            return redirect('blog-index')
    else:
        form = UserRegistationForm()
    return render(request, 'users_app/register.html', {'title':'Register', 
                                                       'form': form})
