from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import Http404
from .models import Student, Registration
from .forms import StudentForm, KakForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        #DO STUFFS
        sender_name = request.POST['sender-name']
        sender_email = request.POST['email']
        sender_subject = request.POST['subject']
        sender_message = request.POST['message'] 
        try:
            send_mail(
                sender_name + ' sending inquiring email on ' + sender_subject ,#subject
                sender_email + ' has sent you an inquiry |  ' + sender_message,#Message
                sender_email,#from email
                ['kakraotvcollege@gmail.com'] ,#to email
                fail_silently = False,

            )
            messages.success(request, sender_name +' your message has been received successfully')
            return render(request,'pages/home.html')  
        except:
            messages.error(request,'Error in sending the message')
            return redirect('index')
    else:
        context = {}
        return render(request,'pages/home.html',context)


#def dashboard(request):
    #students = Student.objects.all()
    #return render(request, 'pages/dashboard.html', {'students': students})

def dashboard(request):
    all_students = Registration.objects.all()
    return render(request, 'pages/dashboard.html', {'all_students': all_students})

def student_detail(request,student_id):
    try:
        student = Registration.objects.get(id=student_id)
    except Registration.DoesNotExist:
        raise Http404('Student Not Found')
    return render(request, 'pages/student_detail.html',{'student': student})

#def student_detail(request,student_id):
    #try:
        #student = Student.objects.get(id=student_id)
    #except Student.DoesNotExist:
        #raise Http404('Student Not Found')
    #return render(request, 'pages/student_detail.html', {'student': student})


def register_form(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST, request.FILES)
        if student_form.is_valid():
            student_form.save()
            #messages.success(request, ('Your data has been received successfully'))
            return redirect('index')
        else:
            #messages.error(request,'Error saving form')
            return redirect('register_form')
    else:
        #student_form = StudentForm()
        #return render(request,'pages/home.html', {'student_form': student_form})
        student_form = StudentForm()
        return render(request,'pages/registration.html', {'student_form': student_form})


   # if request.method == "POST":
        #student_form = StudentForm(request.POST, request.FILES)
		#if student_form.is_valid():
            #student_form.save()
			#messages.success(request, ('Your movie was successfully added!'))
		#else:
			#messages.error(request, 'Error saving form')
		   # return redirect('register_form')
    #else:
        #student_form = StudentForm()
        #return render(request,'pages/registration.html', {'student_form': student_form})

def kakform(request):
    if request.method=="POST":
        kak_form = KakForm(request.POST)
        if kak_form.is_valid():
            kak_form.save()
            return redirect('kakform')
        else:
            return redirect('index')
    else:
        return render(request,'pages/kakform.html',{})
     