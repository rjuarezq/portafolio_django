from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "core/index.html")

def aboutMe(request):
    return render(request, "core/about.html")

def portafolio(request):
    return render(request, "core/portafolio.html")

def contactMe(request):
    return render(request, "core/contact.html")