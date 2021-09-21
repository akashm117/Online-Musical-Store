from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        FirstName = request.POST['fname']
        LastName = request.POST['lname']
        UserName = request.POST['uname']
        Email = request.POST['email']
        Pass1 = request.POST['pass1']
        Pass2 = request.POST['pass2']
        if Pass1 == Pass2:
            if User.objects.filter(username=UserName).exists():
                messages.info(request, "UserName already exists")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, "EmailID already exists")
                return redirect('register')
            else:
                u = User.objects.create_user(username=UserName, first_name=FirstName, last_name=LastName, email=Email,
                                             password=Pass1)
                u.save()
                messages.info(request, "You Have Successfully Registered!")
                return render(request, 'index.html')
        else:
            messages.info(request, "Password Not Matching")
            return redirect('register')


    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        u = auth.authenticate(username=uname, password=password)
        if u is not None:
            request.session['uid']=u.id #its a temporary session in which we storing the userid
            auth.login(request, u)
            return redirect("/")
        else:
            messages.info(request, "Login Failed! Invalid Credentials")
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,"You Have Logged Out! Visit Again!")
    return redirect("/")