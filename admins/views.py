from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from users.models import User


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {
        'title': 'Geek shop - ADMIN'
    }
    return render(request, 'admins/index.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    context = {
        'title': 'Geek shop - users',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'GeekShop - create user',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, user_id):
    selected_user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'Geek shop - update user',
        'selected_user': selected_user,
        'form': form,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


def admin_users_delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.safe_delete()
    return HttpResponseRedirect(reverse('admins:admin_users'))