from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as login_process
from .models import SubUser,BestieAdmin
from main.models import Resort
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BestieForm
from main.models import Packages
# Create your views here.
def login(request):
    return render(request,'useradmin/login.html')

def verify(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        username_check = SubUser.objects.filter(username=username,is_subuser=True).first()
        password_check = SubUser.objects.filter(password=password).first()
        # if  username_check and password_check:
        # else:
        #     messages.error(request,'User Not Found')
        user = authenticate(username=username,password=password)
        if user is not None:
            login_process(request,user)
            # return render(request,'useradmin/dashboard.html')
            return redirect('useradmin:dashboard')
    return render(request,'useradmin/login.html')


@login_required()
def dashboard(request):
    return render(request,'useradmin/dashboard.html')

@login_required()
def add_resort(request):
    if request.method == 'POST' and request.FILES['resort_image']:
        resort_name = request.POST['resort_name']
        resort_description = request.POST['resort_description']
        resort_service_1 = request.POST['resort_service1']
        resort_service_2 = request.POST['resort_service2']
        resort_service_3 = request.POST['resort_service3']
        resort_service_4 = request.POST['resort_service4']
        resort_service_5 = request.POST['resort_service5']
        resort_service_6 = request.POST['resort_service6']
        resort_service_7 = request.POST['resort_service7']
        resort_service_8 = request.POST['resort_service8']
        resort_image = request.FILES['resort_image']
        resort_package = request.POST.get('resort_package')
        resort_aminities_1 = request.POST['resort_aminities1']
        resort_aminities_2 = request.POST['resort_aminities2']
        resort_aminities_3 = request.POST['resort_aminities3']
        resort_aminities_4 = request.POST['resort_aminities4']
        resort_aminities_5 = request.POST['resort_aminities5']
        resort_aminities_6 = request.POST['resort_aminities6']
        resort_aminities_7 = request.POST['resort_aminities7']
        resort_aminities_8 = request.POST['resort_aminities8']
        resort_amount = request.POST['resort_amount']
        # resort_add = BestieAdmin(resort_name=resort_name,resort_description=resort_description,resort_service=resort_service,resort_aminities=resort_aminities,resort_images=resort_image,resort_user=request.user)
        # package = Packages.objects.filter(package_name=resort_package).first()
        # resort_add.resort_package=package
        # resort_add.save()
        resort_add = Resort(resort_name=resort_name,resort_description=resort_description,resort_images=resort_image,resort_service_1=resort_service_1,resort_service_2=resort_service_2,resort_service_3=resort_service_3,resort_service_4=resort_service_4,resort_service_5=resort_service_5,resort_service_6=resort_service_6,resort_service_7=resort_service_7,resort_service_8=resort_service_8,resort_aminities_1=resort_aminities_1,resort_aminities_2=resort_aminities_2,resort_aminities_3=resort_aminities_3,resort_aminities_4=resort_aminities_4,resort_aminities_5=resort_aminities_5,resort_aminities_6=resort_aminities_6,resort_aminities_7=resort_aminities_7,resort_aminities_8=resort_aminities_8,resort_amount=resort_amount,user=request.user)
        package = Packages.objects.filter(package_name=resort_package).first()
        resort_add.resort_package=package
        resort_add.save()
        messages.success(request,'Resort Added')
        return redirect('useradmin:add_resort')
    packages = Packages.objects.all()
    context = {
        'package':packages
    }
    return render(request, 'useradmin/add_resort.html', context) 