from django.shortcuts import render


def index(request):
    return render(request,'frontend/index.html')
def gallery(request):
    return render(request,'frontend/gallery.html')
def contact(request):
    return render(request,'frontend/contact.html')