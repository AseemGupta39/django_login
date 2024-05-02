from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
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

        #   user = User.objects.filter(username=user_name)
          
        #   if user.exists():
        #     #    messages.error(request, "username already exist.")  
        #        return redirect('/register/')

        #   print("\n\n\n\n",first_name,last_name,username,password,"\n\n\n\n")

        #   user = User.objects.create(
        #        first_name=first_name,
        #        last_name=last_name,
        #        username=username,
        #        email = email
        #   )
          
        #   user.set_password(password)
        #   user.save()
        # #   messages.success(request, "account registerd.")
        #   return redirect("register_app/login_page/") 
    return render(request,'register_app/signup.html')

def login_page(request):
    return render(request,'register_app/login.html')

