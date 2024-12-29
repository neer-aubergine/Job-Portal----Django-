from django.shortcuts import render
from .models import Company
from .forms import CompanyForm
from django.shortcuts import get_object_or_404 , redirect
# Create your views here.
def index(request):
    return render(request , 'index.html')

def company_list(request):
    companies = Company.objects.all().order_by("-created_At")
    users_company = Company.objects.filter(user = request.user)
    user_has_company = users_company.exists()
    return render(request , 'company_list.html' , {'companies' : companies , 'user_has_company': user_has_company,})

def company_create(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request , 'company_form.html' , {'form' : form})

def company_edit(request , company_id):
    company = get_object_or_404(Company , pk = company_id , user = request.user)
    if request.method == "POST":
        form = CompanyForm(request.POST , instance=company)
        if form.is_valid():
            company = form.save(commit=False)
            company.user = request.user
            company.save()
            return redirect("company_list")
    else:
        form = CompanyForm(instance=company)
    return render(request , 'company_form.html' , {'form' : form})

def company_delete(request , company_id):
    company = get_object_or_404(Company , pk = company_id , user = request.user)
    if request.method == "POST":
        company.delete()
        return redirect("company_list")
    return render(request , 'company_confirm_delete.html' , {'company' : company})