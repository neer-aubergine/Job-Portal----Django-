from django.shortcuts import render
from .models import Company
from .forms import CompanyForm,UserRegistrationForm
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request , 'index.html')
@login_required
def company_list(request):
    print(request.user)
    print("========================================================")
    companies = Company.objects.all().order_by("-created_At")
    if request.user != "AnonymousUser":
        print("=======================1")
        users_company = Company.objects.filter(user = request.user)
   
    user_has_company = users_company.exists()
    return render(request , 'company_list.html' , {'companies' : companies , 'user_has_company': user_has_company,})

@login_required
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

@login_required
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

@login_required
def company_delete(request , company_id):
    company = get_object_or_404(Company , pk = company_id , user = request.user)
    if request.method == "POST":
        company.delete()
        return redirect("company_list")
    return render(request , 'company_confirm_delete.html' , {'company' : company})


def register(request):
    if request.method =="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request , user)
            return redirect('company_list')
    else:
        form = UserRegistrationForm   
    return render(request , 'registration/register.html' , {'form' : form})
