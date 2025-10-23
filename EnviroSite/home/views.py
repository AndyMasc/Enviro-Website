from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def what_is_it(request):
    return render(request, 'home/whatisCC.html')

def issue(request):
    return render(request, 'home/issue.html')

def solutions(request):
    return render(request, 'home/solutions.html')