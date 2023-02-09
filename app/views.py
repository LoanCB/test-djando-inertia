from django.http import HttpRequest
from inertia import render


def index(request):
    return render(request, "Index", props={"name": "Test"})


def about(request):
    return render(request, "About", props={"pageName": "About"})
