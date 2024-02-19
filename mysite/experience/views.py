from django.shortcuts import render
from experience.models import Experience

def experience(request):

    experience = Experience.objects.all()

    context = {
        "experience": experience
    }

    return render(request, "experience/experience.html", context)
