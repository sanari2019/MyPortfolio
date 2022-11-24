from django.urls import path

from . import views


appapp_name='auctions'
urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("about", views.about, name="about"),
    path("project", views.project, name="project"),
    # path("project/<int:id>", views.project_id, name="project_id"),
    path("cactus", views.cactus, name="cactus"),
    path("myforms", views.myforms, name="myforms"),
    path("createtest", views.createtest, name="createtest"),
    path("createport", views.createport, name="createport"),
    path("createexp", views.createexp, name="createexp"),
    path("createedu", views.createedu, name="createedu"),
    path("createcou", views.createcou, name="createcou"),
    path("createskill", views.createskill, name="createskill"),
    path("contact", views.contact, name="contact"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    

    path('<slug:category_slug>', views.about, name='resume_by_speciality'),
    path('<slug:category_slug>', views.project, name='portfolio_by_speciality'),
    
    
]
