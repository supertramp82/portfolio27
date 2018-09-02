from django.shortcuts import render

from .models import Job


def index(req):
    jobs = Job.objects
    return render(req, 'jobs/index.html', {'jobs': jobs})
