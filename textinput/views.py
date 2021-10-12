from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def text2(request):
    comm = request.GET.get('comments')
    return render(request, 'text2.html', {"result": comm})


