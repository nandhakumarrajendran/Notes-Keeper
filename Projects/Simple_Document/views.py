from django.shortcuts import render, redirect
import datetime
from .forms import Simple_Document
from .models import Document
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def Create_Document(request):
    
    if request.method == 'POST':
        Title = request.POST.get('title')
        Content = request.POST.get('content')
        datetimes = datetime.datetime.now()
        Date = datetimes.strftime("%Y-%m-%d")
        Time = datetimes.strftime('%I:%M:%S')
        Userid = request.user
        data= Document(user = Userid, title =Title, content = Content, date = Date, time = Time)
        data.save()
        return redirect('view_document')
    else:
        forms = Simple_Document()
    return render(request, 'create_document.html', {'form': forms})


@login_required
def View_Document(request):
    try:
        Datas = Document.objects.filter(user_id = request.user)
        Data = {'Tasks': Datas}
        return render(request, 'view_document.html', context= Data)
    
    except Document.DoesNotExist:
        pass
    
    
    return render(request, 'view_document.html')

def Update(request, id):
    if request.method == 'POST':
        
        Title = request.POST.get('title')
        Content = request.POST.get('content')
        datetimes = datetime.datetime.now()
        Date = datetimes.strftime("%Y-%m-%d")
        Time = datetimes.strftime('%I:%M:%S')
        
        data = Document.objects.get(id = id)
        data.title, data.content, data.date, data.time = Title, Content, Date, Time
        data.save()
        return redirect('view_document')
    datas = Document.objects.filter(id = id).first()
    update_data = {'update_document': datas}
        
    return render(request, 'update_document.html', context= update_data)


def Delete(request, id):
    data = Document.objects.filter(id = id).first()
    data.delete()
    return redirect('view_document')

@login_required
def search(request):
    query = request.GET['search']

    if len(query) > 100:
        all = Document.objects.none()
        
    else:
        alltitles = Document.objects.filter(title__icontains = query)
        alluserid = Document.objects.filter(user_id = request.user)
        allposts = alltitles.intersection(alluserid)
        
    if allposts.count() == 0:
        messages.warning(request,'No Search Results...')
        
    datas = {'data': allposts, 'query': query}
    return render(request,'document_search.html', datas)