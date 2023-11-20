from django.shortcuts import render

# Create your views here.
def looping(request):
  d={'name':'marshall'}
  return render(request,'looping.html',context=d)
