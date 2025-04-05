from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


@login_required
def homepage(request):
    return render(request, "tournament_bracket/homepage.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "tournament_bracket/register.html", {"form": form})
