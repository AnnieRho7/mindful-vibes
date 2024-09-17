from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import UserForm, ProfileForm
from .models import UserProfile
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User

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
    

def password_reset_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        form = PasswordResetForm({'email': email})
        
        if form.is_valid():
            user = User.objects.filter(email=email).first()
            if user:
                # Generate the token
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                current_site = get_current_site(request)

                # Email context
                email_subject = 'Password Reset Requested'
                email_body = render_to_string('password_reset_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': uid,
                    'token': token,
                    'protocol': 'https' if request.is_secure() else 'http',
                })

                # Send email
                send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                messages.success(request, "An email has been sent with instructions to reset your password.")
                return redirect('password_reset_done')

            else:
                messages.error(request, "No user is associated with this email address.")
        else:
            messages.error(request, "Invalid email address. Please try again.")
    else:
        form = PasswordResetForm()

    return render(request, 'password_reset.html', {'form': form})

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
