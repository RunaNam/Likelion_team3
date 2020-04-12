from django.shortcuts import render


# Create your views here.

def num3(request):
    return render(request, 'twitter/3.html',{})
