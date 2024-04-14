from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from home.models import ContactEntry
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)

def about(request):
    return render(request, 'about.html')

def contact(request):   
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
                       # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Process the form data (send email, save to database, etc.)
            # For now, let's just print the form data
            print(form.cleaned_data)
            entry = ContactEntry(name=name, email=email, message=message)
            entry.save()
            # Redirect to a success page or any other page after successful submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        name=request.POST.get('name')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        messages.success(request, 'you created your account.')
        return redirect('login')

    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('user')
            messages.success(request, 'Welcome back')

    return render(request,'login.html')

def user(request):
    return render(request,'user.html')

def afilter(request):
    return render(request,'afilter.html')

def result(request):
    return render(request,'result.html')
