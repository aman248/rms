from django.contrib.auth.signals import user_logged_in
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect, render
from .forms import UploadFileForm,ShowResultForm,CreateUserForm
from django.contrib.auth import authenticate,login,logout
import pandas
from .models import Student,School,Marks,Subject,Exam
from django.contrib import messages

# Imaginary function to handle an uploaded file.

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'],form.cleaned_data['test_name'],School.objects.filter(name=request.user.username)[0])
            return redirect('storage:result')
    else:
        form = UploadFileForm()
    return render(request, 'storage/upload.html', {'form': form})
def handle_uploaded_file(f,name_given,skool):
    df = pandas.read_excel(f)
    l = list(df['Student'])
    ls = list(df.columns)
    ls.remove('Student')
    ls.remove('rollno')
    for i in ls:
        s = Subject(name = i)
        s.save()
    e = Exam(name=name_given)
    e.save()
    for index,row in df.iterrows():
        s = Student(
            name = row['Student'],
            rollno = row['rollno'],
            school = skool
            )
        s.save()
        for i in ls:
            m = Marks(
                school = skool,
                subject = Subject.objects.filter(name=i)[0],
                student=Student.objects.filter(name=row['Student'])[0],
                value=row[i],
                exam=e
                )
            m.save()

def result(request):
    if request.method == 'POST':
        form = ShowResultForm(request.POST)
        if form.is_valid():
            data = get_data_or_false(form)
            if data:
                return render(request,'storage/data.html',{'datas':data})
            else:
                messages.info(request,'No record Found')
            
    else:
        form = ShowResultForm()
    return render(request,'storage/result.html',{'form':form})

def get_data_or_false(form):
    schoolname = form.cleaned_data['schoolname']
    rollno = form.cleaned_data['rollno']
    testname = form.cleaned_data['testname']
    schools = School.objects.filter(name=schoolname)
    exams = Exam.objects.filter(name=testname)
    if schools and exams:
        students = schools[0].student_set.filter(rollno=rollno)
        if students:
            m = Marks.objects.filter(school=schools[0].id,exam=exams[0].id,student=students[0].id)
            if m:
                return m
    return False

def registerpage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            s = School.objects.create(name=form.cleaned_data['username'])
            s.save()
            messages.info(request,'School registered')
            return redirect('storage:login')
    else:
        form = CreateUserForm()
    return render(request,'storage/signup.html',{'form':form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.info(request,'login successful')
            return redirect('storage:ufile')
        else:
            messages.info(request,'incorrect username or password.')
    return render(request,'storage/login.html')
def logoutpage(request):
    logout(request)
    messages.info(request,'logout successful')
    return redirect('storage:ufile')








