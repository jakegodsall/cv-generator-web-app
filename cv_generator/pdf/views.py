from django.shortcuts import render
from .forms import ProfileForm

# Create your views here.
def index(request):
    if request.method == "POST":
        ...
    form = ProfileForm()
    return render(request, "pdf/index.html", {"form": form})