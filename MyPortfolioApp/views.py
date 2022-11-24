from multiprocessing import context
from turtle import title
from xmlrpc.client import ProtocolError
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic

from MyPortfolioApp.filter import PortfolioFilter
from .forms import *
from .models import *
from django.contrib import messages
from django.views.generic.detail import DetailView

# Create your views here.


class index(generic.TemplateView):


    template_name = "MyPortfolioApp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        testimonies= Testimonial.objects.filter(is_active=True)
        port = Portfolio.objects.order_by('-date_created')[:6]

        context["testimonies"] = testimonies
        context["port"] = port
    
        return context

def about(request, category_slug=None):
    category=None
    specialities= Specialty.objects.all()
    projects = Resume.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skill = Skill.objects.all()
    course = Courses.objects.all()
 

    if category_slug:
        category = get_object_or_404(Specialty, slug=category_slug)
        projects = projects.filter(speciality=category)
        skill=skill.filter(speciality=category)
        course=course.filter(speciality=category)
        
    return render(request, "MyPortfolioApp/about.html",{"projects":projects, "category":category, "specialities":specialities, "education":education,"experience":experience, "skill":skill, "course":course})





 

def project(request):
   portfolio = Portfolio.objects.all()
   portfolio_filter=PortfolioFilter(request.GET, queryset=portfolio)
   
   context = {
    'portfolio_filter':portfolio_filter,
    # 'portfolio':portfolio
   }
   return render(request, "MyPortfolioApp/projects.html", context)


@login_required
def createtest(request):

    
    if request.method=='POST':

        img_url = request.POST['img_url']
        client_name = request.POST['client_name']
        testimony = request.POST['testimony']

        Testimonial.objects.create(img_url=img_url, client_name=client_name, testimony=testimony )
  


    return render(request, "MyPortfolioApp/forms.html")

@login_required
def createport(request):
  
    
    if request.method=='POST':

        speciality= request.POST['speciality']
        image_url = request.POST['image_url']
        project_name = request.POST['project_name']
        project_url  = request.POST['project_url']

        p=Portfolio(speciality=speciality, image_url=image_url, project_name=project_name, project_url=project_url )
        p.save()
  
    return render(request, "MyPortfolioApp/forms.html")


@login_required
def createexp(request):
  
    
    if request.method=='POST':

        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        job_role = request.POST['job_role']
        company  = request.POST['company']
        achievement  = request.POST['achievement']
        responsibilities  = request.POST['responsibilities']

        Experience.objects.create(start_date=start_date, end_date=end_date, job_role=job_role, company=company, achievement=achievement, responsibilities=responsibilities)
  
    return render(request, "MyPortfolioApp/success.html")


@login_required
def createedu(request):
 
    
    if request.method=='POST':

        start_date = request.POST['start_date ']
        end_date = request.POST['end_date ']
        school = request.POST['school']
        program  = request.POST['program']

        Education.objects.create(start_date=start_date, end_date=end_date, school=school, program=program)
  
    return render(request, "MyPortfolioApp/forms.html")


@login_required
def createcou(request):
 
    
    if request.method=='POST':
        speciality = request.POST['speciality']
        start_date = request.POST['start_date ']
        end_date = request.POST['end_date ']
        course_school = request.POST['course_school']
        course  = request.POST['course']

        Courses.objects.create(speciality=speciality, start_date=start_date, end_date=end_date, course_school=course_school, course=course)
  
    return render(request, "MyPortfolioApp/forms.html")

@login_required
def createskill(request):
 
    
    if request.method=='POST':
        speciality = request.POST['speciality']
        skill_title = request.POST['skill_title']
        skill_set1 = request.POST['skill_set1']
        skill_set2 = request.POST['skill_set2']
        skill_set3 = request.POST['skill_set3']
        skill_set4 = request.POST['skill_set4']
        skill_set5 = request.POST['skill_set5']

        Skill.objects.create(speciality=speciality, skill_title=skill_title, skill_set1=skill_set1, skill_set2=skill_set2, skill_set3=skill_set3,skill_set4=skill_set4,skill_set5=skill_set5)
  


    specialities= Specialty.objects.all()
    context = {
    'specialities':specialities,
    # 'portfolio':portfolio
    }
        
    

        
    return render(request, "MyPortfolioApp/forms.html", context)


def myforms(request):
    specialities= Specialty.objects.all()
    context = {
    'specialities':specialities,
    # 'portfolio':portfolio
   }
    return render(request, "MyPortfolioApp/forms.html", context)

def cactus(request):
    
    url= 'www.cactus-tech.com'
    return HttpResponseRedirect(url)

def contact(request):
    return render(request, "MyPortfolioApp/contact.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "MyPortfolioApp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "MyPortfolioApp/login.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
