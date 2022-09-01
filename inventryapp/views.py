from django.shortcuts import HttpResponse, render

from .models import Phone


# Create your views here.
def index(request):
    return HttpResponse("hello")


def avi(request):
    return HttpResponse("hello avinash")


def phone(request):
    if request.GET:
        name = request.GET['phone']
        data = (Phone.objects.filter(phone=name))
        # for d in data:
        #     print(d.getPhone())
        #     print(type(d))
    return render(request, "phone.html", {"phone": name, "data": data})
