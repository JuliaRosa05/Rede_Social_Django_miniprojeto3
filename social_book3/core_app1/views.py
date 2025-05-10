from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileUpdateForm
from .models import Profile
from .models import Post
from django.core.exceptions import ObjectDoesNotExist
from .forms import PostForm




def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Associa o post ao usuário logado
            post.save()
            return redirect('index')  # Redireciona para o feed após salvar o post
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})

@login_required(login_url='login')
def index(request):
    posts = Post.objects.all().order_by('-created_at')  
    return render(request, "index.html", {'posts': posts})

@login_required
def settings_view(request):
    try:
        profile = request.user.profile  
    except ObjectDoesNotExist:
        return redirect('home')  

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('setting')  
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'setting.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos.'})
    return render(request, 'login.html')

