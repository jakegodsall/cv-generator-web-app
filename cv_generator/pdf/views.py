from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.
def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, "pdf/index.html", {"form": form})
    form = ProfileForm()
    return render(request, "pdf/index.html", {"form": form})