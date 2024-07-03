from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ImageUploadForm
from .models import Image

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('image_list')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

@login_required
def image_list(request):
    images = Image.objects.filter(user=request.user)
    return render(request, 'image_list.html', {'images': images})

