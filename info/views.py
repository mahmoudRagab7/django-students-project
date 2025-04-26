# info/views.py
from django.shortcuts import render

from .models import FAQ, Quote

# Create your views here.


def home_view(request):
    quotes = Quote.objects.all()
    return render(request, "info/home.html", {"quotes": quotes})


def about_view(request):
    faqs = FAQ.objects.all()
    return render(request, "info/about.html", {"faqs": faqs})
