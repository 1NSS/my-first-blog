from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
<<<<<<< HEAD
=======


>>>>>>> 0d32a521784c8e6e4bf4c6a6d6fe53c577394d37

# Create your views here.

def text2(request):
    comm = request.GET.get('comments')
    return render(request, 'text2.html', {"result": comm})


<<<<<<< HEAD

=======
>>>>>>> 0d32a521784c8e6e4bf4c6a6d6fe53c577394d37
