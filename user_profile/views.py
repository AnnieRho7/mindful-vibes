from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserForm, ProfileForm
from .models import UserProfile


# @login_required
# def user_profile(request):
#     user = request.user

#     # Ensure the UserProfile exists
#     user_profile, created = UserProfile.objects.get_or_create(user=user)

#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=user)
#         profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile has been updated successfully!')
#             return redirect('user_profile')
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         user_form = UserForm(instance=user)
#         profile_form = ProfileForm(instance=user_profile)

#     return render(request, 'user_profile/user_profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })

@login_required
def user_profile(request):
    user = request.user

    # Ensure the UserProfile exists
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user_profile)

    return render(request, 'user_profile/user_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    

# def password_reset_done_view(request):
#     return render(request, 'templates/index.html', {})

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        # Delete the associated UserProfile if it exists
        UserProfile.objects.filter(user=user).delete()
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('home')  # Redirect to a page after account deletion (e.g., home or login page)
    else:
        return HttpResponseForbidden("You are not allowed to access this page.")
