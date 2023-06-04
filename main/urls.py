from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('activity/',views.activity,name="activity"),
    path('resorts/',views.resorts,name="resorts"),
    path('gallery/',views.gallery,name="gallery"),
    path('about-us/',views.aboutus,name="about-us"),
    path('contact-us/',views.contactus,name="contact-us"),
]
