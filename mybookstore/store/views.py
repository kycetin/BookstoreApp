from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,JsonResponse

import requests
import json
import math
import pprint

def home(request):
    response = requests.get(f"https://api.itbook.store/1.0/new")
    data = response.json()
    return render(request,'index.html',{"ls":data["books"]})
