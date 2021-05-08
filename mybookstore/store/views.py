from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

import requests
import json
import math
import pprint

def create_range(total):
    range_list = []
    pag_size = math.ceil(total/10)
    if pag_size > 100:
        pag_size = 100
    for i in range(1,pag_size+1):
        if i > 100:
            pag_size = 100
            break
        range_list.append(i)
    return pag_size,range_list

def home(request):
    response = requests.get(f"https://api.itbook.store/1.0/new")
    data = response.json()
    total = int(data["total"])
    pag_size,range_list = create_range(total)
    return render(request,'index.html',{"ls":data["books"],"pg":pag_size,"range":range_list,"current_page":1 })

def store_search(request,search):
    response = requests.get(f"https://api.itbook.store/1.0/search/{search}")
    data = response.json()
    total = int(data["total"])
    pag_size,range_list = create_range(total)
    return render(request,'index.html',{"ls":data["books"],"pg":pag_size,"keyword":search,"range":range_list,"current_page":1 })

def store_search_bar(request,search):
    response = requests.get(f"https://api.itbook.store/1.0/search/{search}")
    data = response.json()
    total = int(data["total"])
    pag_size,range_list = create_range(total)
    return render(request,'index.html',{"ls":data["books"],"pg":pag_size,"keyword":search,"range":range_list,"current_page":1 })

def store_search_page(request,search,page):
    response = requests.get(f"https://api.itbook.store/1.0/search/{search}/{page}")
    data = response.json()
    total = int(data["total"])
    pag_size,range_list = create_range(total)
    return render(request,'index.html',{"ls":data["books"],"pg":pag_size,"range":range_list,"keyword":search,"current_page":page })

def store_search_bar(request,page):
    if request.method == 'POST':
        search = request.POST.get('search_input')
        response = requests.get(f"https://api.itbook.store/1.0/search/{search}/1")
        data = response.json()
        total = int(data["total"])
        pag_size,range_list = create_range(total)
        return render(request,'index.html',{"ls":data["books"],"pg":pag_size,"range":range_list,"keyword":search,"current_page":page})
