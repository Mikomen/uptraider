from django.shortcuts import render
from uptraider.models import MenuItem



def show_top_menu(request):
    menu_items = MenuItem.objects.all()

    return render(request, 'base.html', {'menu_items': menu_items})

# def indexhandler(request):
#     menu_items = MenuItem.objects.all()
#
#     return render(request, 'index.html', {'menu_items': menu_items})
