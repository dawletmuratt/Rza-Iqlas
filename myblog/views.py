from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from myblog.forms import PostForm

from .forms import*


def home_detailpage(request, pk):
    posts = Post.objects.get(id=pk)
    context = {
        'posts' : posts
    }
    return render(request, 'myblog/home_detail.html', context)

def aboutpage(request):
    return render(request, 'myblog/about.html')

def contactpage(request):
    return render(request, 'myblog/contact.html')

def servicespage(request):
    return render(request, 'myblog/services.html')

def loginpage(request):
    return render(request, 'myblog/login.html')

def product_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myapp:myapp'))
    else:
        form = PostForm()
    context = {'form': form}
    return render(request,'admin/products_add.html', context)

def home(request, slug=None):
    if slug:
        category = Category.objects.get(slug=slug)
        product = Product.objects.filter(cat=category)
    else:
        product = Product.objects.all()
    context={'category':Category.objects.all(), 'product':product}
    return render(request, 'myblog/home.html', context=context)