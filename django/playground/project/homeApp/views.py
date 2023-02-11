from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate, login, logout


class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder':'email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(
        attrs={'placeholder':'username'}))
    password1 = forms.CharField(
        required= True,
        label = "",
        widget=forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required= True,
        label = "",
        widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'})
    )
    class Meta:
        model = get_user_model() 
        fields = ('username', 'email', 'password1', 'password2')

def registerView(request):
    form = CreateNewUser()
    
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("helloHtml")
    context = {
        'form' : form,
    }
    return render(request, 'register.html', context)


def loginView(request):
    if request.method == "POST":
        # print(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("helloHtml")
        else:
            return HttpResponse("Something went wrong")
        
         
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('loginView')

# Create your views here.
def helloWorld(request):
    return HttpResponse("Hello World")

def helloName(request, name):
    return HttpResponse(f"Hello, {name}")



def helloHtml(request):
    username = request.user
    return render(request, 
                  "home.html", context= {
        "username" : username
                  })

def helloNameHtml(request, name):
    return render(request,
     "hello.html", context={
        "name" : name
    })
