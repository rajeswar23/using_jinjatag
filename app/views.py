from django.shortcuts import render

# Create your views here.
def condtion(request):
    d={'a':10,'b':20}
    return render(request,'condtion.html',d)