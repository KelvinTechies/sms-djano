from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from .forms import StudentForms
from .models import Students


def index(request):
    students=Students.objects.all();
    return render(request, 'students/index.html', {'students':students})
    


def view_student(request, id):
    student=Students.object.get(pk=id);

    return HttpResponseRedirect(reverse('index'));


def add(request):
    if request.method =='POST':
        form= StudentForms(request.POST)
        if form.is_valid():
            new_student_number=form.cleaned_data['student_Number']
            new_first_name=form.cleaned_data['first_name']
            new_last_name=form.cleaned_data['last_name']
            new_email=form.cleaned_data['email']
            new_fiels_of_study=form.cleaned_data['fiels_of_study']
            new_gpa=form.cleaned_data['gpa']


            new_student=Students(
            student_Number=new_student_number,
            first_name=new_first_name,
            last_name=new_last_name,
            email=new_email,
            fiels_of_study=new_fiels_of_study,
            gpa=new_gpa
            
                )
            new_student.save()
        return render(request, 'students/add.html', {'forms':StudentForms(), 'success':True})

    else:
        form=StudentForms()
        return render(request, 'students/add.html', {'forms':StudentForms()})


def edit(request, pk):
    if request.method=='POST':
        student=Students.objects.get(id=pk)
        form=StudentForms(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return render(request, 'student/index.html', {form:form, 'success':True})
    else:
        student=Students.objects.get(id=pk)
        form=StudentForms(instance=student)
        return render(request, 'students/edit.html', {'form':form})
            
def delete(request, pk):
    if request.method=='POST':
        student=Students.objects.get(id=pk)
        student.delete()
    return HttpResponseRedirect(reverse('index'))