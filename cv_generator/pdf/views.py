from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm

# Create your views here.
def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "pdf/create_profile.html", {"form": form})
    form = ProfileForm()
    return render(request, "pdf/create_profile.html", {"form": form})

def display_cv(request, profile_id=1):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, "pdf/cv.html", {"profile": profile})