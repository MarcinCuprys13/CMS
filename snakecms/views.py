from django.shortcuts import render

def page_creator(request):
    return render(request, 'page_creator.html')
