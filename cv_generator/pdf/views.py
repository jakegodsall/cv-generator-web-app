import io
import pdfkit
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

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
    template = loader.get_template("pdf/cv.html")
    rendered_template = template.render({"profile": profile}, request)
    options = {
        'page-size': 'Letter',
        'encoding': 'utf-8'
    }
    pdf = pdfkit.from_string(rendered_template, False, options)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    return response