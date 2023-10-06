from django.shortcuts import render
from menu.models import MenuItem


def menu(request):
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'menu/menu.html', {'menu_items': menu_items})
