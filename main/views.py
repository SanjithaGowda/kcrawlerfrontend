from django.shortcuts import render
from django.views.generic import ListView, DetailView
from uuid import uuid4
from .forms import EntryItemForm
from .models import EntryItem, ArticleItem
from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')

# Create your views here.
def CreateEntry(request):
    form = EntryItemForm(request.POST or None)
    if request.method == 'POST':
        ids = str(uuid4())
        taskId = scrapyd.schedule('kcrawler', 
        'mainspider', keyword = request.POST.get('keyword', None), uid = ids)
        entry = EntryItem()
        entry.unique_id = ids
        entry.keyword = request.POST.get('keyword', None)
        entry.task_id = taskId
        entry.status = 'processing'
        entry.save()

    objects = EntryItem.objects.all()
    return render(request, 'main/index.html', {'objects': objects, 'form': form})

def ListArticles(request, pk):
    keyword = EntryItem.objects.get(pk=pk).keyword
    objects = ArticleItem.objects.filter(entry=pk)
    half_length = int(len(objects)/2)
    
    return render(request, 'main/list.html', {'keyword': keyword,'half_length' : half_length, 'objects': ArticleItem.objects.filter(entry=pk)})

def Home(request):
    form = EntryItemForm(request.POST or None)
    if request.method == 'POST':
        ids = str(uuid4())
        taskId = scrapyd.schedule('kcrawler', 
        'mainspider', keyword = request.POST.get('keyword', None), uid = ids)
        entry = EntryItem()
        entry.unique_id = ids
        entry.keyword = request.POST.get('keyword', None)
        entry.task_id = taskId
        entry.status = 'processing'
        entry.save()
    objects = EntryItem.objects.all()
    objectlist = [objects[0], objects[1]]
    return render(request, 'main/home.html', {'form': form, 'objectlist':objectlist})

def History(request):
    objects = EntryItem.objects.all()
    half_length = int(len(objects)/2)
    return render(request, 'main/history.html',{'objects': objects, 'half_length': half_length, 'length': len(objects)  })