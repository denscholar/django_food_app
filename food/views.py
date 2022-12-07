from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'food/index.html', context)
