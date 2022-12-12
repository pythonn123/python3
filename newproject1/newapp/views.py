from django.shortcuts import render
from . models import place,team


# Create your views here.
def Home(request):
    obj=place.objects.all()
    obj1=team.objects.all()

    return render(request,"index.html",{'result':obj,'result1':obj1})
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res1=x-y
#     res2=x*y
#     return render(request,"About.html",{'result':res,'result1':res1,'result2':res2})
#

# def About(request):
#     return render(request,"About.html")
# def Contact(request):
#     return render(request,"Contact.html")
# def Details(request):
#     return render(request,"Details.html")
# def Thanks(request):
#     return render(request,"Thanks.html")