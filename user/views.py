from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from user.forms import CreateUserForm, UserProfileForm

User = get_user_model()


class UserListView(generic.ListView):
    template_name = 'user/index.html'
    model = User
    context_object_name = 'users'


def user_create(request):
    form = CreateUserForm()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('/')
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'user/user_create.html', context)


def user_update(request, pk):
    user = User.objects.get(id=pk)
    form = CreateUserForm(instance=user)

    profile_form = UserProfileForm(instance=user.user_profile)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=user.user_profile)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('/')
    context = {'form': form, 'profile_form': profile_form, 'update':True}
    return render(request, 'user/user_create.html', context)


def user_delete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('/')
