from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from openlink.core.models import Profile, Tool


def home(request):
    return render(request, "openlink/home.html")


def contact(request):
    return render(request, "openlink/contact.html")


@login_required
def get_user_profile(request, username):
    p_list = Profile.objects.filter(user=request.user)
    t_list = Tool.objects.filter(author__user=request.user)
    context = {"username": username, "profile_list": p_list, "tool_list": t_list}
    return render(request, "openlink/user_profile.html", context)
