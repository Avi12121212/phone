from django.shortcuts import HttpResponse, render, redirect

from .models import Myuser
from .models import Phone


# Create your views here.
def index(request):
    return HttpResponse("hello")


def avi(request):
    return HttpResponse("hello avinash")


def phone(request):
    name = ''
    data = []
    data1 = []
    if request.GET:
        name = request.GET['phone']
        data = (Phone.objects.filter(phone=name))
        # for d in data:
        #     print(d.getPhone())
        #     print(type(d))
    return render(request, "phone.html", {"phone": name, "data": data, "session": request.session.items()})


def user(request):
    data = []
    username = ""
    password = ""
    result = "wrong"
    if request.GET:
        username = request.GET["username"]
        password = request.GET["password"]
        data = Myuser.objects.filter(username=username) & Myuser.objects.filter(password=password)
        print(len(data), "******")
        if len(data) != 0:
            result = "correct"
            print(data[0].getName())
            request.session["username"] = data[0].getName()
            return redirect('http://127.0.0.1:8000/phone/')
        else:
            return render(request, "invalide.html")
        # for da in data:
        #     print((da))
        # print(da.get("name"))
    return render(request, "user.html",
                  {"data": data, "session": request.session.items(), "r": result, "username": username,
                   "password": password})


def signup(request):
    if request.GET:
        name = request.GET["name"]
        username = request.GET["username"]
        password = request.GET["password"]
        data = Myuser(name=name, username=username, password=password)
        data.save()
    return render(request, "signup.html")


def signout(request):
    return render(request, "signout.html")
