from django.shortcuts import render
from .models import Profile

def index(request):
    """Display page for Profile (lists view)"""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Single page display for a Profile Item (detailed view)"""
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
