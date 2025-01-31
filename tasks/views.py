from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def prueba(request):
    # return HttpResponse("Hola alejo")    
    return render(request, "signup.html")