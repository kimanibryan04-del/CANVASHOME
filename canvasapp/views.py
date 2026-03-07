from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def property(request):
    return render(request, 'properties.html')
def service(request):
    return render(request, 'services.html')
def agent(request):
    return render(request, 'agents.html')
def contact(request):
    return render(request, 'contact.html')
def privacy(request):
    return render(request, 'privacy.html')
def terms(request):
    return render(request, 'terms.html')
def agentprofile(request):
    return render(request, 'agent-profile.html')
def servicedetails(request):
    return render(request, 'service-details.html')
def propertdetails(request):
    return render(request, 'property-details.html')


