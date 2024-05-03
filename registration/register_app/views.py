from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_page')
def home_page(request):
    return render(request,'register_app/home.html')

def signup_page(request):
    if request.method == "POST":
        data = request.POST
        first_name= data.get('first_name')
        last_name = data.get('last_name')
        user_name =  data.get('user_name')
        email = data.get('email')
        password =  data.get('password')
        print("\n\n\n\n",first_name,last_name,user_name,password,"\n\n\n\n")

        user = User.objects.filter(username=user_name)
        
        if user.exists():
            print("user exist")  
            messages.error(request,"user already exist")
            # return HttpResponse("user already exist")
            return redirect('signup')
            # return render(request,'register_app/signup.html')


        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=user_name,
            email = email
        )
        
        user.set_password(password)
        user.save()
        messages.success(request, "account created successfully.")
        return redirect('login_page')
    return render(request,'register_app/signup.html')

def login_page(request):
    if request.method == "POST":
        data = request.POST
        user_name = data.get('user_name')
        password = data.get('password')
        user = authenticate(request,username=user_name,password=password)
        # print(user)
        if user is not None:
            context = {'user':user_name}
            login(request,user)
            return render(request,'register_app/home.html',context=context)

            # return redirect('home_page')
        else:
            print("\n\nusername or password is incorrect\n\n")
            messages.error(request,"username or password is incorrect")
            return redirect('login_page')
            # return HttpResponse("username or password is incorrect")
    return render(request,'register_app/login.html')

def logout_page(request):
    logout(request)
    return redirect('login_page')