from django.contrib import admin
from django.urls import path
from canvasapp import views

urlpatterns = [
path('admin/', admin.site.urls),
path('',views.index,name='home'),
path('about/',views.about,name='about'),
path('property/',views.property,name='properties'),
path('service/',views.service,name='services'),
path('agents/',views.agent,name='agents'),
path('contact/',views.contact,name='contact'),
path('privacy/',views.privacy,name='privacy'),
path('terms/',views.terms,name='terms'),
path('profile/',views.agentprofile,name='agentprofile'),
path('details/',views.servicedetails,name='servicedetails'),
path('propertydetails/',views.propertdetails,name='propertydetails'),


]
