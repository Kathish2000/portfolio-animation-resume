from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def experience(request):
    return render(request, 'experience.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('portfolio:contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
