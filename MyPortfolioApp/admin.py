from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

admin.site.register(Testimonial,)
admin.site.register(User, UserAdmin,)
admin.site.register(Specialty,)
admin.site.register(Portfolio,)
admin.site.register(Resume,)
admin.site.register(Courses,)
admin.site.register(Experience,)
admin.site.register(Education,)
admin.site.register(Skill,)
