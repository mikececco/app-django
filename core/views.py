from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html') #automatically searches for a templates folder
