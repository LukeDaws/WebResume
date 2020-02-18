from django.shortcuts import render

def mainmenu(request):
    return render(request, 'webresume/mainmenu.html', {})

# Create your views here.
