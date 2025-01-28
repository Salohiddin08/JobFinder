from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from .models import Post
from .forms import CommentForm,PostForm
from django.views import generic 
from django.contrib.auth.decorators import login_required

# Create your views here.

 
def blog_list(request):
    blog_list = Post.objects.all()  # Post modelidan barcha bloglarni olish
    paginator = Paginator(blog_list, 10)  # Har bir sahifada 10 ta post
    page_number = request.GET.get('page')  # URL'dan sahifa raqamini olish
    page_obj = paginator.get_page(page_number)  # Sahifani olish

    context = {'blogs': page_obj}  # Sahifalash natijasini contextga qo'shish
    return render(request, 'blog/blog_list.html', context)  # Natijani shablonga yuborish


@login_required
def blog_detail(request,slug):
    blog_detail=Post.objects.get(slug=slug)
    if request.method=='POST':
        form=CommentForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.post=blog_detail
            myform.username=str(request.user)
            myform.save()
            return redirect('blogs:blog_detail',slug=slug)
            form=CommentForm() #this line is for clear all form fields after submitting
            print('Succesfully Submit')
    else:
        form=CommentForm()


    context={'blog':blog_detail,'CommentForm':form}
    return render(request,'blog/blog_detail.html',context)

@login_required
def create_post(request):


    if request.method=="POST":

        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            
            myform=form.save(commit=False)
            myform.author=request.user
            myform.save()
            form=PostForm() #this line is for clear all form fields after submitting
            return redirect(reverse('blogs:blog_list'))
            
            
    else:
        form=PostForm()
    
    return render(request,'blog/create_post.html',{'CREATEPOSTFORM':form})
