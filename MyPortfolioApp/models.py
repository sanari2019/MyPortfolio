from http import client
from urllib import request
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import  reverse
import django_filters
from django.utils import timezone


# Create your models here.

class User(AbstractUser):
    pass



class Testimonial(models.Model):
    img_url=models.URLField(max_length = 200, db_index=True)
    client_name=models.CharField(max_length=64)
    testimony = models.TextField(db_index=True, help_text=("Required"), blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.client_name}"

class Specialty(models.Model):
   
    spec_name = models.CharField(max_length=64,unique=True,db_index=True)
    slug=models.SlugField(unique=True)

    class Meta:
        ordering=('spec_name',)

    def __str__(self):
        return f"{self.spec_name}"

    def get_absolute_url(self):
        return reverse('resume_by_speciality', args=[self.slug])
        

class Portfolio(models.Model):
    speciality = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    image_url=models.URLField(max_length = 200, db_index=True)
    date_created=models.DateTimeField(default=timezone.now)
    project_name=models.CharField(max_length=64)
    project_url=models.URLField(max_length = 200, db_index=True)
    
    def __str__(self):
        return f"{self.project_name}"
  

class Resume(models.Model):
    speciality = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    job_title=models.CharField(max_length=64)
    about_me = models.TextField(db_index=True, help_text=("Required"), blank=True)
    # phone_number=models.PhoneNumberField()
    Location = models.CharField(max_length=64)
    email = models.EmailField(max_length = 254)
    
    def __str__(self):
        return f"{self.job_title}"
  

class Experience(models.Model):
    
    start_date = models.DateField()
    end_date = models.DateField()
    job_role=models.CharField(max_length=64)
    company=models.CharField(max_length=64)
    achievement=models.TextField(db_index=True, help_text=("Required"), blank=True)
    responsibilities=models.TextField(db_index=True, help_text=("Required"), blank=True)
    

    @property
    def yearstarted(self):
        return self.start_date.strftime('%Y')

    @property
    def monthstarted(self):
        return self.start_date.strftime('%B')
    
    @property
    def yearended(self):
        return self.end_date.strftime('%Y')
    
    @property
    def monthended(self):
        return self.start_date.strftime('%B')

        
    def __str__(self):
        return f"{self.job_role} - {self.company}"

class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    school=models.CharField(max_length=64)
    program=models.CharField(max_length=64)
    
    @property
    def yearstarted(self):
        return self.start_date.strftime('%Y')
    
    @property
    def yearended(self):
        return self.end_date.strftime('%Y')

        
    def __str__(self):
        return f"{self.program} - {self.school}"
    


class Courses(models.Model):
    speciality = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    course_school=models.CharField(max_length=64)
    course=models.CharField(max_length=64)
    

    @property
    def yearended(self):
        return self.end_date.strftime('%Y')
    
    @property
    def yearstarted(self):
        return self.start_date.strftime('%Y')

    def __str__(self):
        return f"{self.course} "
    


class Skill(models.Model):
    speciality = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    skill_title = models.CharField(max_length=64,unique=True,db_index=True)
    skill_set1 = models.CharField(max_length=64, blank=True)
    skill_set2 = models.CharField(max_length=64, blank=True)
    skill_set3 = models.CharField(max_length=64, blank=True)
    skill_set4 = models.CharField(max_length=64, blank=True)
    skill_set5 = models.CharField(max_length=64, blank=True)

         
    def __str__(self):
        return f"{self.skill_title}"

