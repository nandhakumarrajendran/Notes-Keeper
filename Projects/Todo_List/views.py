from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import login_required
from .models import Todo_Task
import random

# Create your views here.
def todo(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Please Login First!')
        return redirect('login')
    
    if request.method == 'POST':
        Title = request.POST.get('title')
        Task = request.POST.get('task')
        datetimes = datetime.datetime.now()
        Date = datetimes.strftime("%Y-%m-%d")
        Time = datetimes.strftime('%I:%M:%S')
        color = ['warning', 'success', 'secondary', 'info', 'dark']
        colors = random.choice(color)
        UserId = request.user
        Data = Todo_Task(UserId = UserId, Title = Title, Task = Task, Date = Date, Time = Time, Bgcolor = colors)
        Data.save()

        return redirect('task_views')
    return render(request, 'todo.html')


@login_required
def task_views(request):
    
    try:
        Datas = Todo_Task.objects.filter(UserId_id = request.user)
        Data = {'Tasks': Datas}
        return render(request, 'todo_views.html', context= Data)
    
    except Todo_Task.DoesNotExist:
        pass
    
    return render(request, 'todo_views.html')

def Update(request, id):
    if request.method == 'POST':
        Title = request.POST.get('title')
        Task = request.POST.get('task')
        datetimes = datetime.datetime.now()
        Date = datetimes.strftime("%Y-%m-%d")
        Time = datetimes.strftime('%I:%M:%S')
        color = ['warning', 'success', 'secondary', 'info', 'dark']
        colors = random.choice(color)
        
        data = Todo_Task.objects.get(id = id)
        data.Title, data.Task, data.Date, data.Time, data.Bgcolor = Title, Task, Date, Time, colors
        data.save()
        return redirect('task_views')
    datas = Todo_Task.objects.filter(id = id).first()
    update_data = {'update_task': datas}
    return render(request, 'todo.html',context=update_data)

def Delete(request, id):
    data = Todo_Task.objects.filter(id = id).first()
    data.delete()
    return redirect('task_views')

@login_required
def search(request):
    query = request.GET['search']

    if len(query) > 100:
        all = Todo_Task.objects.none()
        
    else:
        alltitles = Todo_Task.objects.filter(Title__icontains = query)
        alluserid = Todo_Task.objects.filter(UserId_id = request.user)
        allposts = alltitles.intersection(alluserid)
        
    if allposts.count() == 0:
        messages.warning(request,'No Search Results...')
        
    datas = {'data': allposts, 'query': query}
    return render(request,'todo_search.html', datas)


