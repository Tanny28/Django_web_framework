from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')

def menu(request):
    menu_items = Menu.objects.all()  # Fetch all menu items
    items_dict = {"menu": menu_items}  # Store items in a dictionary
    return render(request, "menu.html", items_dict)  # Pass data to template

def about(request):
    about_content = {
        'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."
    }
    return render(request, 'about.html', {'content': about_content})

def menu(request):
    return render(request, 'menu.html')
