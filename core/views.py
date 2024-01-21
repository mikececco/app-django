from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html') #automatically searches for a templates folder

def contact(request):
    return render(request, 'core/contact.html')
