from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from store.models import User

import requests
import requests_cache
import json
import math
import pprint
import datetime

requests_cache.install_cache('bookstore_cache', backend='sqlite', expire_after=180)

current_page = 0
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
    
    global current_page
    current_page = 1
    response = requests.get(f"https://api.itbook.store/1.0/new")
    data = response.json()
    total = int(data["total"])
    pag_size,range_list = create_range(total)
    return render(request,'index.html',{"ls":data["books"],"pg":pag_size,"range":range_list,"current_page":1 })

def store_search(request,search):

    global current_page
    current_page = 1
    response = requests.get(f"https://api.itbook.store/1.0/search/{search}")
    data = response.json()
    total = int(data["total"])
    pag_size,range_list = create_range(total)
    return render(request,'index.html',{"ls":data["books"],"pg":pag_size,"keyword":search,"range":range_list,"current_page":1 })

def store_search_bar(request,search):
    global current_page
    current_page = 1
    response = requests.get(f"https://api.itbook.store/1.0/search/{search}")
    data = response.json()
    total = int(data["total"])
    pag_size,range_list = create_range(total)
    return render(request,'index.html',{"ls":data["books"],"pg":pag_size,"keyword":search,"range":range_list,"current_page":1 })

def store_search_page(request,search,page):
    global current_page
    current_page = page
    response = requests.get(f"https://api.itbook.store/1.0/search/{search}/{page}")
    data = response.json()
    total = int(data["total"])
    pag_size,range_list = create_range(total)
    return render(request,'index.html',{"ls":data["books"],"pg":pag_size,"range":range_list,"keyword":search,"current_page":page })

def store_search_bar(request,page):
    
    global current_page
    current_page = page
    if request.method == 'POST':
        search = request.POST.get('search_input')
        response = requests.get(f"https://api.itbook.store/1.0/search/{search}/1")
        data = response.json()
        total = int(data["total"])
        pag_size,range_list = create_range(total)
        return render(request,'index.html',{"ls":data["books"],"pg":pag_size,"range":range_list,"keyword":search,"current_page":page})

def add_bookmark(request):
    
    user = User.objects.get(username="cetin")
    button_id = request.POST['button_id']
    response = requests.get(f"https://api.itbook.store/1.0/books/{button_id}")
    book = response.json()
    total = int(user.bookmarks['total'])
    user_books = user.bookmarks['books']
    if user.bookmarks['total'] == 0:
            user_books.append(book)
            user.bookmarks['books'] = user_books
            user.bookmarks['total'] += 1
            user.save()
            return HttpResponse(json.dumps({"response":"added","data":button_id}), content_type='application/json')
    else:
        for i in range(len(user_books)):
            if user_books[i]['isbn13'] == button_id:
                return HttpResponse(json.dumps({"response":"exist","data":button_id}), content_type='application/json')
                break
    user_books.append(book)
    user.bookmarks['books'] = user_books
    user.bookmarks['total'] += 1
    user.save()
    user = User.objects.get(username="cetin")
    return HttpResponse(json.dumps({"response":"added","data":button_id}), content_type='application/json')

def bookmarks(request):
    
    global current_page
    current_page = 1
    user = User.objects.get(username="cetin")
    books = user.bookmarks
    total = int(user.bookmarks['total'])
    user_books = user.bookmarks['books']
    pag_size,range_list = create_range(total)
    data = []
    page=1
    for i in range((page*10)-10,(page*10)):
        if i == total:
            break
        data.append(user_books[i])
    return render(request,'bookmark.html',{"ls":data,"pg":pag_size,"range":range_list,"keyword":user,"current_page":1})

def bookmarks_page(request,page):
    global current_page
    current_page = page
    user = User.objects.get(username="cetin")
    books = user.bookmarks
    total = int(user.bookmarks['total'])
    user_books = user.bookmarks['books']
    pag_size,range_list = create_range(total)
    data = []
    for i in range((page*10)-10,(page*10)):
        if i == total:
            break
        data.append(user_books[i])
    return render(request,'bookmark.html',{"ls":data,"pg":pag_size,"range":range_list,"keyword":user,"current_page":page})

def delete_bookmark(request):
    
    user = User.objects.get(username="cetin")
    button_id = request.POST['button_id']
    # page = int(request.POST['current'])
    global current_page
    total = int(user.bookmarks['total'])
    user_books = user.bookmarks['books']
    if len(user_books) == 0:
            del user_books[0]
            user.bookmarks['books'] = user_books
            user.bookmarks['total'] -= 1
            user.save()
    for i in range(len(user_books)):
        if user_books[i]['isbn13'] == button_id:
            del user_books[i]
            user.bookmarks['books'] = user_books
            user.bookmarks['total'] -= 1
            user.save()
            return HttpResponse(json.dumps({"response":button_id}), content_type='application/json')
    user = User.objects.get(username="cetin")
    user_books = user.bookmarks['books']
    total = int(user.bookmarks['total'])
    pag_size = math.ceil(total/10)
    data = []
    pag_size,range_list = create_range(total)
    for i in range((page*10)-10,(page*10)):
        if i == total:
            break
        data.append(user_books[i])
    return render(request,'bookmark.html',{"ls":data,"pg":pag_size,"range":range_list,"keyword":user,"current_page":page})

def read_more(request):
    
    button_id = request.POST['button_id']
    response = requests.get(f"https://api.itbook.store/1.0/books/{button_id}")
    data = response.json()
    global current_page
    return HttpResponse(json.dumps({"data":data,"current_page":current_page}), content_type='application/json')
