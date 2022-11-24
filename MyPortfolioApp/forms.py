import re
from django import forms

from MyPortfolioApp.filter import PortfolioFilter
from .models import *

class PortfolioForm(forms.ModelForm):

    class Meta:
      model=Portfolio
      fields="__all__"


class CoursesForm(forms.ModelForm):
    class Meta:
      model=Courses
      fields="__all__"

class SkillForm(forms.ModelForm):
    class Meta:
      model=Skill
      fields="__all__"


# class PortfolioForm(forms.ModelForm):
#     class Meta:
#       model=Portfolio
#       fields="__all__"

