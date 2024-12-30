from django.shortcuts import render
from .models import Job
from .forms import JobForm
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request , 'jobs.html')
@login_required
def jobs_list(request):
    jobs = Job.objects.all().order_by("-created_At")
    paginator = Paginator(jobs,6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request , 'jobs.html' , {'jobs' : page_obj })

@login_required
def job_create(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.company = request.user.company
            job.save()
            return redirect('jobs')
    else:
        form = JobForm()
    return render(request , 'job_form.html' , {'form' : form})

@login_required
def job_edit(request , job_id):
    job = get_object_or_404(Job , pk = job_id , user = request.user)
    if request.method == "POST":
        form = JobForm(request.POST , instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect("jobs")
    else:
        form = JobForm(instance=job)
    return render(request , 'job_form.html' , {'form' : form})

@login_required
def job_delete(request , job_id):
    job = get_object_or_404(Job , pk = job_id , user = request.user)
    if request.method == "POST":
        job.delete()
        return redirect("jobs")
    return render(request , 'job_confirm_delete.html' , {'job' : job})

