from user.models import Task
from django.shortcuts import render
from datetime import date

# Create your views here.
def home(request):
    return render(request,'user/home.html')

def add_task(request):
    msg = ''
    if request.method == 'POST':
       task_title = request.POST['title']
       task_desc = request.POST['desc'] 
       task_date = request.POST['date']
    #    task_completed =request.POST['completed_date']
    #    task_status = request.POST['status']

       
       new_task = Task(task = task_title,description = task_desc,date = task_date)
       new_task.save()
        #    completed_date = task_completed,
        #    status = task_status,
       
       msg = 'task added'
    return render(request,'user/add_task.html',{'status':msg})

def view_task(request):
    return render(request,'user/view_task.html')

def profile(request):
    return render(request,'user/profile.html')

