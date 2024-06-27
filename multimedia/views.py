# multimedia/views.py
# multimedia/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, VideoForm
from .models import Video

def index(request):
    videos = Video.objects.all()  # Retrieve all videos from the database
    context = {
        'videos': videos,  # Pass the videos queryset to the template
    }
    return render(request, 'multimedia/index.html', context)

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after successful upload
    else:
        form = VideoForm()
    return render(request, 'multimedia/upload_video.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

