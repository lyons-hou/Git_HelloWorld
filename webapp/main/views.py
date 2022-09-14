from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def main(request):
  return HttpResponseRedirect("http://172.16.33.223/~jenkins.bios/Jenkins/CoffeeLake/MLC8/MLC8/MLC8/255/MLC8_00311_Image.zip")
