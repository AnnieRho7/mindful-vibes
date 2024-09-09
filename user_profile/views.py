from django.shortcuts import render

def user_profile_view(request):
    return render(request, 'user_profile/user_profile.html') 
