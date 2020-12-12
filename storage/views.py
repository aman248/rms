from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm,ShowResultForm
import pandas
from .models import Student,School,Marks,Subject,Exam

# Imaginary function to handle an uploaded file.

def upload_file(request):
    if request.method == 'POST':
        print('i am post bitch #####################################')
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print('i am valid bitch ****************************')
            print(Student)
            handle_uploaded_file(request.FILES['file'],form.cleaned_data['test_name'],School.objects.filter(name='Prince')[0])
            return HttpResponse('file upload successfull........')
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
    print('exam is created with id ',e.pk)
    e.save()
    for index,row in df.iterrows():
        s = Student(
            name = row['Student'],
            rollno = row['rollno'],
            school = skool
            )
        print('student is created with id ',s.pk)
        s.save()
        for i in ls:
            m = Marks(
                school = skool,
                subject = Subject.objects.filter(name=i)[0],
                student=Student.objects.filter(name=row['Student'])[0],
                value=row[i],
                exam=e
                )
            print('mark is created with id ',m.pk)
            m.save()

def result(request):
    if request.method == 'POST':
        form = ShowResultForm(request.POST)
        print('*******************point3')
        if form.is_valid():
            print('$$$$$$$$$$$$$$$point1')
            data = get_data_or_false(form)
            if data:
                print('&&&&&&&&&&&&&&&&&&&&point2')
            return render(request,'storage/data.html',{'datas':data})
            
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
            

