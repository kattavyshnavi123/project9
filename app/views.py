from django.shortcuts import render

# Create your views here.
def Ram(request):
    d={'name':'Ram','age':22}
    return render(request,'Ram.html',context=d)
