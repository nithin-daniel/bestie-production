from django.shortcuts import render,redirect
from main.models import Activity,ClientTestimonials,GalleryPhotos,Packages,Resort,Event,LatestNews,ContactUs
from django.http import HttpResponse
# Create your views here.
def home(request):
    testimonials = ClientTestimonials.objects.all()
    packages = Packages.objects.all()
    events = Event.objects.all()[:2]
    latest_news = LatestNews.objects.all()[:2]
    images = GalleryPhotos.objects.all()

    context = {
        'testimonials':testimonials,
        'packages':packages,
        'events':events,
        'latest_news':latest_news,
        "images":images,
    }
    return render(request,'main/home.html',context)

def activity(request):
    obj = Activity.objects.all()
    context = {
        'obj':obj
    }
    return render(request,'main/activity.html',context)

def gallery(request):
    images = GalleryPhotos.objects.all()
    context = {
        "images":images,
    }

    return render(request,'main/gallery.html',context)

def aboutus(request):
    testimonials = ClientTestimonials.objects.all()
    context = {
        'testimonials':testimonials
    }
    return render(request,'main/about-us.html',context)
def resorts(request):
    get_resorts = Resort.objects.all()
    context = {
        'get_resorts':get_resorts,
    }
    return render(request,'main/resorts.html',context)

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        # contact_us = ContactUs()
        ContactUs.objects.create(name=name,email=email,phone_number=number,message=message)
        # contact_us.save()
        return redirect("contact-us")
    else:
        return render(request,'main/contact-us.html')    

def success_page(request):
    return render(request,'main/success-page-popup.html')

def resort_detail(request,package_slug):
    # get_package = Packages.objects.filter(package_slug=package_slug)
    # get_resort = Resort.objects.filter(resort_package__id__in=get_package).all()
    get_resort = Resort.objects.filter(resort_slug=package_slug)
    context = {
        'get_resort':get_resort,
    }
    return render(request,'main/resort-details.html',context)

def room_detail(request,room_details):
    get_details = Resort.objects.filter(resort_package__package_slug=room_details)
    context = {
        'get_resorts':get_details
    }
    return render(request,'main/room.html',context)

def events(request):
    get_events = Event.objects.all()
    context = {
        'get_events':get_events
    }
    return render(request,'main/events.html',context)

def events_detail(request,details):
    event_details_page = Event.objects.filter(event_name=details).first()
    upcomming_event = Event.objects.all()[:5]
    context = {
        'event_details_page':event_details_page,
        'upcomming_event':upcomming_event
    }
    return render(request,'main/events-details.html',context)