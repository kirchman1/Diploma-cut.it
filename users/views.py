from django.shortcuts import render, redirect
from .forms import UserRegForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == "POST":
        form = UserRegForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:     
        form = UserRegForm()

    return render(
        request, 
        'users/registration.html', 
        {
            'title': 'Registration Page',
            'form': form,
            
            }
    )


@login_required
def profile(request):

    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if updateUserForm.is_valid():
            updateUserForm.save()
            messages.success(request, f'Your account was successfully updated!')
            return redirect('profile')

    else:
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
        'updateUserForm': updateUserForm,
        'title': 'Your Profile'
    }

    return render(request, 'users/profile.html', data)
