from django.shortcuts import render,redirect
from .models import StudentData

def indexpage(request):
    data=StudentData.objects.all()
    return render(request,'indexpage.html',{'data':data})

def add_student(request):
    if request.method=='GET':
        return render(request,'add.html')

    else:
        StudentData(
        first_name=request.POST.get('fname'),
        last_name=request.POST.get('lname'),
        course=request.POST.get('cname'),
        fee=request.POST.get('fee'),
        iname=request.POST.get('iname'),
        mobile=request.POST.get('mobile'),
        email=request.POST.get('email'),
        a1=request.POST.get('a1'),
        a2=request.POST.get('a2'),
        a3=request.POST.get('a3'),
        a4=request.POST.get('a4'),
        loc=request.POST.get('loc')
        ).save()
        return redirect('indexpage')

def update_student(request,id):
    row=StudentData.objects.get(id=id)
    return render(request, 'update_student.html', {'row': row})

def updated(request,id):
    data=StudentData.objects.get(id=id)
    data.first_name = request.POST.get('fname')
    data.last_name = request.POST.get('lname')
    data.course = request.POST.get('cname')
    data.fee = request.POST.get('fee')
    data.iname = request.POST.get('iname')
    data.mobile = request.POST.get('mobile')
    data.email = request.POST.get('email')
    data.a1 = request.POST.get('a1')
    data.a2 = request.POST.get('a2')
    data.a3 = request.POST.get('a3')
    data.a4 = request.POST.get('a4')
    data.loc = request.POST.get('loc')

    data.save()
    return redirect('indexpage')

def deletestudent(request,id):
    data=StudentData.objects.get(id=id)
    data=delete()
    return redirect('indexpage')
