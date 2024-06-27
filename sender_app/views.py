from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .tasks import send_high_level_priority_message, send_low_level_priority_message


def register(requset):
    if requset.method == 'POST':
        form = CustomUserCreationForm(requset.POST)
        if form.is_valid():
            user = form.save()
            login(requset, user)
            send_high_level_priority_message(user)
            send_low_level_priority_message(user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(requset, 'user/register.html', {'form': form})

