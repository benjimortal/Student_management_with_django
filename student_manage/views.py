from django.shortcuts import render

# Create your views here.

def list_student(request):
    return render(request, 'crud/base.html')