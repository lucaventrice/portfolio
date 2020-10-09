from django.http.response import HttpResponse
from django.shortcuts import render

def project_list(request):
    return render(request, 'projects/index.html')
