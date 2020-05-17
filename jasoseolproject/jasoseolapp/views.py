from django.shortcuts import render, redirect, get_object_or_404
from .forms import JasoseolForm
from .models import Jasoseol
from django.http import Http404

def index(request):
    myjss = Jasoseol.objects.all()

    return render(request, 'index.html',{'myjss':myjss})


def create(request):
    if request.method == "POST":
        myform = JasoseolForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('index')

    myform = JasoseolForm()
    return render(request, 'create.html' ,{'myform':myform})


def detail(request, jss_id):
    # jss = get_object_or_404(Jasoseol, pk=jss_id)
    try:
        jss = Jasoseol.objects.get(pk=jss_id)
    except:
        raise Http404

    return render(request, 'detail.html',{'jss':jss})


def delete(request, jss_id):
    # jss = get_object_or_404(Jasoseol, pk=jss_id)
    jss = Jasoseol.objects.get(pk=jss_id)
    jss.delete()

    return redirect('index')


def update(request, jss_id):
    jss = Jasoseol.objects.get(pk=jss_id)
    # jss = get_object_or_404(Jasoseol, pk=jss_id)
    if request.method == "POST":
        update_form = JasoseolForm(request.POST, instance=jss)
        if update_form.is_valid():
            update_form.save()
            return redirect('index')
    
    myform = JasoseolForm(instance=jss)    
    return render(request, 'create.html', {'myform':myform})
    