from django.shortcuts import render

def main(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def text(request):
    return render(request, 'main/text.html')