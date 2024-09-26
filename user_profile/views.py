from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from .models import UserProfile


@login_required
def user_profile(request):
    """
    View for users to view and update their own profile.
    """
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(
            request.POST,
            request.FILES,
            instance=user_profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request,
                'Your profile has been updated successfully!'
            )
            return redirect('user_profile')
        else:
            messages.error(
                request,
                'Please correct the errors below.'
            )
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user_profile)

    return render(
        request,
        'user_profile/user_profile.html',
        {
            'user_form': user_form,
            'profile_form': profile_form
        }
    )


@login_required
def delete_account(request):
    """
    View to delete the user's account.
    """
    if request.method == 'POST':
        user = request.user
        UserProfile.objects.filter(user=user).delete()
        user.delete()
        messages.success(
            request,
            'Your account has been deleted successfully.'
        )
        return redirect('home')
    else:
        return HttpResponseForbidden(
            "You are not allowed to access this page."
        )


def view_user_profile(request, username):
    """
    View to display a public user profile by their username.
    """
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)

    return render(request, 'user_profile/view_user_profile.html', {
        'user_profile': user_profile,
        'user': user
    })


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
