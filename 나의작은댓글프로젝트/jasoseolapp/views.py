from django.shortcuts import render, redirect, get_object_or_404
from .forms import JasoseolForm,CommentForm,ReCommentForm
from .models import Jasoseol,Comment,ReComment
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
    
    mycom_form = CommentForm()
    myrecom_form = ReCommentForm()
    context = {'comment_form':mycom_form, 'jss':jss,'recomment_form':myrecom_form}
    return render(request, 'detail.html',context)


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
    

def create_comment(request, jss_id):
    filled_form = CommentForm(request.POST) 

    if filled_form.is_valid():
        filled_form.save()
    
    return redirect('detail', jss_id)


def delete_comment(request, com_id,jss_id):
    mycom = Comment.objects.get(id = com_id)
    mycom.delete()
    return redirect('detail', jss_id)

def create_recomment(request, jss_id):
    filled_form = ReCommentForm(request.POST) 

    if filled_form.is_valid():
        filled_form.save()
    
    return redirect('detail', jss_id)