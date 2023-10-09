from django.urls import path
from . import views
app_name = 'useradmin'
urlpatterns = [
    path('',views.login,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('resort_delete/<uuid:id>/',views.resort_delete,name='resort_delete'),
    path('verify/',views.verify,name='verify'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_resort/<uuid:id>/',views.add_resort,name='add_resort'),

]
