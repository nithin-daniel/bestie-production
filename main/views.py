from django.shortcuts import render,redirect
from main.models import Activity,ClientTestimonials,GalleryPhotos,Packages,Resort
# Create your views here.
def home(request):
    testimonials = ClientTestimonials.objects.all()
    packages = Packages.objects.all()
    context = {
        'testimonials':testimonials,
        'packages':packages
    }
    return render(request,'main/home.html',context)

def activity(request):
    obj = Activity.objects.all()
    context = {
        'obj':obj
    }
    return render(request,'main/activity.html',context)

def gallery(request):
    global all_images,rooms,activities,events,interior,restaurant
    all_images = GalleryPhotos.objects.all()
    rooms = GalleryPhotos.objects.filter(image_category__category_name="Rooms")
    activities = GalleryPhotos.objects.filter(image_category__category_name="Activities")
    events = GalleryPhotos.objects.filter(image_category__category_name="Events")
    interior = GalleryPhotos.objects.filter(image_category__category_name="Interior")
    restaurant = GalleryPhotos.objects.filter(image_category__category_name="Restaurant")
    context = {
        "all_images":all_images,
        "rooms":rooms,
        "activities":activities,
        'events':events,
        'interior':interior,
        'restaurant':restaurant
    }

    return render(request,'main/gallery.html',context)

def aboutus(request):
    testimonials = ClientTestimonials.objects.all()
    context = {
        'testimonials':testimonials
    }
    return render(request,'main/about-us.html',context)
def resorts(request):
    return render(request,'main/resorts.html')
def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        return redirect("home")
    else:
        return render(request,'main/contact-us.html')    

def success_page(request):
    return render(request,'main/success-page-popup.html')

def resort_detail(request,package_slug):
    package_instance = Packages.objects.get(package_slug=package_slug)
    get_resort = Resort.objects.filter(resort_package=package_instance)
    context = {
        'get_resort':get_resort,
    }
    return render(request,'main/room.html',context)

def room_detail(request,room_details):
    get_details = Resort.objects.get(resort_name=room_details)
    print(get_details.resort_images)
    context = {
        'get_details':get_details
    }
    print(get_details)
    return render(request,'main/room-detail.html',context)

def events(request):
    return render(request,'main/events.html')

def events_detail(request):
    return render(request,'main/events-details.html')