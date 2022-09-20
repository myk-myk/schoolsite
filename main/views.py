from django.shortcuts import render
from .models import BlogPost
from .forms import BlogPostForm, MyUserForm

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def coaching(request):
    return render(request, 'main/coaching.html')


def time(request):
    return render(request, 'main/time.html')


def contact(request):
    error = ''
    if request.method == 'POST':
        user_form = MyUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
        else:
            error = 'Помилка при введенні даних'
    user_form = MyUserForm()
    user = {
        'user_form': user_form,
        'error': error
    }
    return render(request, 'main/contact.html', user)


def blog(request):
    err = ''
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            err = 'Помилка при введенні даних'
    form = BlogPostForm()
    blog_p = BlogPost.objects.all()
    post = {
        'form': form,
        'error': err,
        'blog': blog_p
    }
    return render(request, 'main/blog.html', post)
