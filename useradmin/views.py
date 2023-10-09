from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as login_process ,logout
from .models import SubUser
from main.models import Resort
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .forms import BestieForm
from main.models import Packages
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('useradmin:dashboard')
    return render(request,'useradmin/login.html')

def verify(request):
    if request.user.is_authenticated:
        return redirect('useradmin:dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            subuser = SubUser.objects.filter(username=username,is_subuser=True)
            if not subuser:
                messages.error(request,'You have no permission')
                return redirect('useradmin:login')
            login_process(request,user)
            # return render(request,'useradmin/dashboard.html')
            return redirect('useradmin:dashboard')
        else:
            messages.error(request,'User Not Found')
            return redirect('useradmin:login')
    return render(request,'useradmin/login.html')


@login_required()
def dashboard(request):
    user = request.user
    resort = Resort.objects.filter(user=user)
    context = {
        'resort':resort
    }
    return render(request,'useradmin/dashboard.html',context)

@login_required()
def add_resort(request,id):
    # if request.method == 'POST' and request.FILES['resort_image_1']:

    #     resort_name = request.POST['resort_name']
    #     resort_description = request.POST['resort_description']
    #     resort_service_1 = request.POST['resort_service1']
    #     resort_service_2 = request.POST['resort_service2']
    #     resort_service_3 = request.POST['resort_service3']
    #     resort_service_4 = request.POST['resort_service4']
    #     resort_service_5 = request.POST['resort_service5']
    #     resort_service_6 = request.POST['resort_service6']
    #     resort_service_7 = request.POST['resort_service7']
    #     resort_service_8 = request.POST['resort_service8']
    #     resort_image_1 = request.FILES['resort_image_1']
    #     resort_image_2 = request.FILES['resort_image_2']
    #     resort_image_3 = request.FILES['resort_image_3']
    #     resort_image_4 = request.FILES['resort_image_4']
    #     resort_image_5 = request.FILES['resort_image_5']
    #     resort_package = request.POST.get('resort_package')
    #     resort_aminities_1 = request.POST['resort_aminities1']
    #     resort_aminities_2 = request.POST['resort_aminities2']
    #     resort_aminities_3 = request.POST['resort_aminities3']
    #     resort_aminities_4 = request.POST['resort_aminities4']
    #     resort_aminities_5 = request.POST['resort_aminities5']
    #     resort_aminities_6 = request.POST['resort_aminities6']
    #     resort_aminities_7 = request.POST['resort_aminities7']
    #     resort_aminities_8 = request.POST['resort_aminities8']
    #     resort_amount = request.POST['resort_amount']
    #     resort_update = Resort.objects.all().filter(resort_id=id).first()
    #     resort_update.resort_name = resort_name
    #     resort_update.resort_description = resort_description
    #     resort_update.resort_service_1 = resort_service_1
    #     resort_update.resort_service_2 = resort_service_2
    #     resort_update.resort_service_3 = resort_service_3
    #     resort_update.resort_service_4 = resort_service_4
    #     resort_update.resort_service_5 = resort_service_5
    #     resort_update.resort_service_6 = resort_service_6
    #     resort_update.resort_service_7 = resort_service_7
    #     resort_update.resort_service_8 = resort_service_8
    #     resort_update.resort_image_1 = resort_image_1
    #     resort_update.resort_image_2 = resort_image_2
    #     resort_update.resort_image_3 = resort_image_3
    #     resort_update.resort_image_4 = resort_image_4
    #     resort_update.resort_image_5 = resort_image_5
    #     resort_update.resort_package = resort_package
    #     resort_update.resort_package = resort_package
    #     resort_update.resort_aminities_1 = resort_aminities_1
    #     resort_update.resort_aminities_2 = resort_aminities_2
    #     resort_update.resort_aminities_3 = resort_aminities_3
    #     resort_update.resort_aminities_4 = resort_aminities_4
    #     resort_update.resort_aminities_5 = resort_aminities_5
    #     resort_update.resort_aminities_6 = resort_aminities_6
    #     resort_update.resort_aminities_7 = resort_aminities_7
    #     resort_update.resort_aminities_8 = resort_aminities_8
    #     resort_update.resort_amount = resort_amount
    #     resort_update.save()
    # #     resort_add = Resort(resort_name=resort_name,resort_description=resort_description,resort_image_1=resort_image_1,resort_image_2=resort_image_2,resort_image_3=resort_image_3,resort_image_4=resort_image_4,resort_image_5=resort_image_5,resort_service_1=resort_service_1,resort_service_2=resort_service_2,resort_service_3=resort_service_3,resort_service_4=resort_service_4,resort_service_5=resort_service_5,resort_service_6=resort_service_6,resort_service_7=resort_service_7,resort_service_8=resort_service_8,resort_aminities_1=resort_aminities_1,resort_aminities_2=resort_aminities_2,resort_aminities_3=resort_aminities_3,resort_aminities_4=resort_aminities_4,resort_aminities_5=resort_aminities_5,resort_aminities_6=resort_aminities_6,resort_aminities_7=resort_aminities_7,resort_aminities_8=resort_aminities_8,resort_amount=resort_amount,user=request.user)
    # #     package = Packages.objects.filter(package_name=resort_package).first()
    # #     resort_add.resort_package=package
    # #     resort_add.save()
    #     messages.success(request,'Resort Added')

    #     return redirect('useradmin:add_resort')
    
    # packages = Packages.objects.all()
    # edit_resort = Resort.objects.filter(resort_slug=resort_id)
    # print(edit_resort)
    # context = {
    #     'package':packages
    # }
    return render(request, 'useradmin/add_resort.html') 
@login_required()
def resort_delete(request,id):  
    print(id)
    
    edit_resort = Resort.objects.all().filter(resort_id=id).first()
    packages = Packages.objects.all()
    if request.method == 'POST':
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
            # resort_image_1 = request.FILES['resort_image_1']
            # resort_image_2 = request.FILES['resort_image_2']  
            # resort_image_3 = request.FILES['resort_image_3']
            # resort_image_4 = request.FILES['resort_image_4']
            # resort_image_5 = request.FILES['resort_image_5']
            resort_package = request.POST.get('resort_package')
            resort_aminities_1 = request.POST['resort_aminities1']
            resort_aminities_2 = request.POST['resort_aminities2']
            resort_aminities_3 = request.POST['resort_aminities3']
            resort_aminities_4 = request.POST['resort_aminities4']
            resort_aminities_5 = request.POST['resort_aminities5']
            resort_aminities_6 = request.POST['resort_aminities6']
            resort_aminities_7 = request.POST['resort_aminities7']
            resort_aminities_8 = request.POST['resort_aminities8']
            # resort_amount = request.POST['resort_amount']

            resort_update = Resort.objects.all().filter(resort_id=id).first()

            resort_update.resort_name = resort_name
            resort_update.resort_description = resort_description
            resort_update.resort_service_1 = resort_service_1
            resort_update.resort_service_2 = resort_service_2
            resort_update.resort_service_3 = resort_service_3
            resort_update.resort_service_4 = resort_service_4
            resort_update.resort_service_5 = resort_service_5
            resort_update.resort_service_6 = resort_service_6
            resort_update.resort_service_7 = resort_service_7
            resort_update.resort_service_8 = resort_service_8
            # if resort_image_1:
            #     resort_update.resort_image_1 = resort_image_1
            # if resort_image_2:
            #     resort_update.resort_image_2 = resort_image_2
            # if resort_image_3:
            #     resort_update.resort_image_3 = resort_image_3
            # if resort_image_4:
            #     resort_update.resort_image_4 = resort_image_4
            # if resort_image_5:
            #     resort_update.resort_image_5 = resort_image_5
            # resort_update.resort_package = resort_package
            resort_update.resort_aminities_1 = resort_aminities_1
            resort_update.resort_aminities_2 = resort_aminities_2
            resort_update.resort_aminities_3 = resort_aminities_3
            resort_update.resort_aminities_4 = resort_aminities_4
            resort_update.resort_aminities_5 = resort_aminities_5
            resort_update.resort_aminities_6 = resort_aminities_6
            resort_update.resort_aminities_7 = resort_aminities_7
            resort_update.resort_aminities_8 = resort_aminities_8
            # resort_update.resort_amount = resort_amount
            resort_update.save()
        #     resort_add = Resort(resort_name=resort_name,resort_description=resort_description,resort_image_1=resort_image_1,resort_image_2=resort_image_2,resort_image_3=resort_image_3,resort_image_4=resort_image_4,resort_image_5=resort_image_5,resort_service_1=resort_service_1,resort_service_2=resort_service_2,resort_service_3=resort_service_3,resort_service_4=resort_service_4,resort_service_5=resort_service_5,resort_service_6=resort_service_6,resort_service_7=resort_service_7,resort_service_8=resort_service_8,resort_aminities_1=resort_aminities_1,resort_aminities_2=resort_aminities_2,resort_aminities_3=resort_aminities_3,resort_aminities_4=resort_aminities_4,resort_aminities_5=resort_aminities_5,resort_aminities_6=resort_aminities_6,resort_aminities_7=resort_aminities_7,resort_aminities_8=resort_aminities_8,resort_amount=resort_amount,user=request.user)
        #     package = Packages.objects.filter(package_name=resort_package).first()
        #     resort_add.resort_package=package
        #     resort_add.save()
            messages.success(request,'Resort Added')
            return redirect('useradmin:dashboard')       
    else:
        edit_resort = Resort.objects.all().filter(resort_id=id).first()
        packages = Packages.objects.all()

        context = {
                "edit_resort":edit_resort,
                'package':packages
            }
        return render(request, 'useradmin/add_resort.html', context) 
   

def logout_view(request):
    logout(request)
    return redirect('useradmin:login')