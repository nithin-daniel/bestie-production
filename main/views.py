from django.shortcuts import render,redirect
from main.models import Activity,ClientTestimonials,GalleryPhotos,Packages,Resort,Event,LatestNews,ContactUs
# Create your views here.
def home(request):
    testimonials = ClientTestimonials.objects.all()
    packages = Packages.objects.all()
    events = Event.objects.all()[:2]
    latest_news = LatestNews.objects.all()[:2]
    context = {
        'testimonials':testimonials,
        'packages':packages,
        'events':events,
        'latest_news':latest_news
    }
    return render(request,'main/home.html',context)

def activity(request):
    obj = Activity.objects.all()
    context = {
        'obj':obj
    }
    return render(request,'main/activity.html',context)

def gallery(request):
    # global all_images,rooms,activities,events,interior,restaurant
    # all_images = GalleryPhotos.objects.all()
    # rooms = GalleryPhotos.objects.filter(image_category__category_name="Rooms")
    # activities = GalleryPhotos.objects.filter(image_category__category_name="Activities")
    # events = GalleryPhotos.objects.filter(image_category__category_name="Events")
    # interior = GalleryPhotos.objects.filter(image_category__category_name="Interior")
    # restaurant = GalleryPhotos.objects.filter(image_category__category_name="Restaurant")
    # context = {
    #     "all_images":all_images,
    #     "rooms":rooms,
    #     "activities":activities,
    #     'events':events,
    #     'interior':interior,
    #     'restaurant':restaurant
    # }

    return render(request,'main/gallery.html')

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
    get_resort = Resort.objects.filter(resort_slug=package_slug)
    context = {
        'get_resort':get_resort,
    }
    return render(request,'main/resort-details.html',context)

def room_detail(request,room_details):
    get_details = Resort.objects.get(resort_name=room_details)
    print(get_details.resort_images)
    context = {
        'get_details':get_details
    }
    return render(request,'main/room-detail.html',context)

def events(request):
    get_events = Event.objects.all()
    context = {
        'get_events':get_events
    }
    return render(request,'main/events.html',context)

def events_detail(request,details):
    event_details_page = Event.objects.get(event_name=details)
    context = {
        'event_details_page':event_details_page
    }
    return render(request,'main/events-details.html',context)