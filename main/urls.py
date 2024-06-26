from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('',views.home,name="home"),
    path('activity/',views.activity,name="activity"),
    path('resorts/',views.resorts,name="resorts"),
    path('gallery/',views.gallery,name="gallery"),
    path('about-us/',views.aboutus,name="about-us"),
    path('contact-us/',views.contactus,name="contact-us"),
    path('resort-detail/<slug:package_slug>/',views.resort_detail,name="resort-detail"),
    path('room-details/<str:room_details>/',views.room_detail,name="room-details"),
    path('events/',views.events,name="events"),
    path('events-details/<str:details>/',views.events_detail,name="events-details"),
]
