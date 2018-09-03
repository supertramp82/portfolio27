from django.shortcuts import render

from .models import Job


def index(req):
    #jobs = Job.objects
    jobs = Job.objects.all().order_by('summary')
    return render(req, 'jobs/index.html', {'jobs': jobs})
