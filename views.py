from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Item, List

def index(request, list_id = 1):
    lists = List.objects.all()
    parent_list = get_object_or_404(List, pk=list_id)
    items = Item.objects.filter(todo_list=parent_list)
    context = {'lists':lists, 'list':parent_list, 'items':items}
    return render(request, 'todo/index.html', context)

def list(request, list_id):
    parent_list = get_object_or_404(List, pk=list_id)
    items = Item.objects.filter(todo_list=parent_list)
    context = {'list':parent_list, 'items':items}
    return render(request, 'todo/list.html', context)

def add_list_form(request):
    return render(request, 'todo/add_list.html')

@csrf_exempt
def add(request, list_id):
    target_list = get_object_or_404(List, pk=list_id)
    item = Item(todo_list=target_list, content=request.POST['content'])
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
    new_list = List(name=request.POST['name'], description=request.POST['description'])
    new_list.save()
    return HttpResponseRedirect(reverse('todo:index'))

@csrf_exempt
def remove_list(request):
    target_list = get_object_or_404(List, pk=request.POST['list_id'])
    target_list.delete()
    return render(request, 'todo/list_list.html', {'lists': List.objects.all()})
