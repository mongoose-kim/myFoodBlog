from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .models import Picture
from .forms import NewBlog

def home(request):
    picture = Picture.objects.all()
    return render(request, 'home.html', {'blog':picture})

def footprint(request):
    blog_list = Blog.objects.all()
    #페이지 3개로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지 변수에 담음
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'footprint.html', {'blogs':blog_list, 'posts':posts})

#새로운 데이터 저장=POST
#글쓰기 페이지 띄워줌=GET

def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
        return redirect('footprint')
    else:
        form = NewBlog()
        return render(request, 'create.html', {'form':form})

def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)

    form = NewBlog(request.POST, request.FILES, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('footprint')
    else:
        form = NewBlog(instance=blog)
        return render(request, 'create.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('footprint')

def bookkyung(request):
    return render(request, 'bookkyung.html')
    
def maum(request):
    return render(request, 'maum.html')
    
def popolo(request):
    return render(request, 'popolo.html')