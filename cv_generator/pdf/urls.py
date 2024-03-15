from django.urls import path
from .views import create_profile, display_cv

app_name = "pdf"
urlpatterns = [
    path('create', create_profile, name="create_profile"),
    path('cv/<int:profile_id>', display_cv, name="display_cv")
]