from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Item, List

def index(request, list_id = 1):
    if request.POST.get('set_id', False):
        request.session['id'] = request.POST['id']

    if not request.session.get('id', False):
        return HttpResponseRedirect(reverse('todo:login'))

    try:
        lists = List.objects.filter(user_id=request.session['id'])
    except:
        lists = False

    try:
        initial_list = lists[0]
        items = Item.objects.filter(todo_list=initial_list)
    except:
        initial_list = False
        items = []

    id = request.session['id']
    context = {'lists':lists, 'list':initial_list, 'items':items, 'id':id}
    return render(request, 'todo/index.html', context)

def list(request, list_id):
    parent_list = get_object_or_404(List, pk=list_id)
    items = Item.objects.filter(todo_list=parent_list)
    context = {'list':parent_list, 'items':items}
    return render(request, 'todo/list.html', context)

def list_only(request, list_id):
    target_list = get_object_or_404(List, pk=list_id)
    items = Item.objects.filter(todo_list=target_list)
    return render(request, 'todo/list_only.html', {'items':items, 'list':target_list})

def login(request):
    return render(request, 'todo/login.html', {})

@csrf_exempt
def add(request, list_id):
    target_list = get_object_or_404(List, pk=list_id)
    item = Item(todo_list=target_list, content=request.POST['content'], user_id=request.session['id'])
    item.save()
    items = Item.objects.filter(todo_list=target_list)
    return render(request, 'todo/list_only.html', {'items':items, 'list':target_list})

@csrf_exempt
def remove(request, list_id):
    target_list = get_object_or_404(List, pk=list_id)
    item = get_object_or_404(Item, pk=request.POST['item_id'])
    item.done = True
    item.save()
    items = Item.objects.filter(todo_list=target_list)
    return render(request, 'todo/list_only.html', {'items':items, 'list':target_list})

@csrf_exempt
def delete(request, list_id):
    target_list = get_object_or_404(List, pk=list_id)
    item = get_object_or_404(Item, pk=request.POST['item_id'])
    item.delete()
    items = Item.objects.filter(todo_list=target_list)
    return render(request, 'todo/list_only.html', {'items':items, 'list':target_list})

@csrf_exempt
def add_list(request):
    new_list = List(name=request.POST['name'], description=request.POST['description'], user_id=request.session['id'])
    new_list.save()
    return HttpResponseRedirect(reverse('todo:index'))

@csrf_exempt
def remove_list(request):
    target_list = get_object_or_404(List, pk=request.POST['list_id'])
    target_list.delete()
    lists = List.objects.filter(user_id=request.session['id'])
    return render(request, 'todo/list_list.html', {'lists': lists})
