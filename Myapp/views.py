from django.shortcuts import render
from .forms import Imageform
from .models import Image

# Create your views here.
def home(request):
    if request.method =="POST":
        form = Imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = Imageform()
    Img =Image.objects.all()
    return render(request, 'home.html', {'Img':Img,'form':form})
    
