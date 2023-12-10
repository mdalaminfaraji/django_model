from django.shortcuts import render, redirect
from .import models
from first_app.forms import StudentForm
# Create your views here.
def home(request):
        if request.method=='POST':
                form = StudentForm(request.POST)
                if form.is_valid():
                        form.save()
                        print(form.cleaned_data)
        else:
                form=StudentForm()
        return render(request, "home.html", {"form":form})

# def delete_student(request, roll):
#         std= models.Student.objects.get(pk = roll).delete()
#         return redirect("homepage")


