from django.shortcuts import render


def homepage(request):
    return render(request, "tournament_bracket/homepage.html")
