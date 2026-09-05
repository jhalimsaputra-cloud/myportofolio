from django.shortcuts import render


def landing_page(request):
    return render(request, "index.html")

def education_page(request):
    return render(request, "education.html")