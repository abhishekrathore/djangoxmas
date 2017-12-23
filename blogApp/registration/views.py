from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt


def index(request):
    students = Student.objects.all()
    str = ""
    for student in students:
        str += student.name+'<br>'

    return HttpResponse(str)

@csrf_exempt
def create(request):
    print(request.POST)
    student = Student()
    student.name = request.POST.get('name')
    student.age = request.POST.get('age')
    student.save()
    context = {"name":student.name,"age":student.age}
    # return render(request,'show.html',context)
    return redirect('profile',student.name)


def register(request):
    return render(request,'create.html')

def profile(request,username):
    student = Student.objects.get(name=username)
    context = {"name":student.name,"age":student.age}
    return render(request,'show.html',context)
