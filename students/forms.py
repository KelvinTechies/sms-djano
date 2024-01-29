from django import forms


from .models import Students


class StudentForms(forms.ModelForm):
    class Meta:
        model=Students
        fields=['student_Number','first_name', 'last_name', 'email', 'fiels_of_study', 'gpa']
        labels={
        'student_Number':'Student Number',
        'first_name':"First Name",
        'last_name':"Last Name",
        'email':"Email",
        'fiels_of_study': "Field Of Study",
        'gpa':"GPA"
            }
        widgets={
        'student_Number':forms.NumberInput(attrs={'class':"form-control"}),
        'first_name':forms.TextInput(attrs={'class':"form-control"}),
        'last_name':forms.TextInput(attrs={'class':"form-control"}),
        'email':forms.EmailInput(attrs={'class':"form-control"}),
        'fiels_of_study':forms.TextInput(attrs={'class':"form-control"}),
        'gpa':forms.NumberInput(attrs={'class':"form-control"})
            }