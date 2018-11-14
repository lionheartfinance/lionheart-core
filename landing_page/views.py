from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'landing_page/index.html')
	
def register(request):
	return render(request, 'landing_page/register.html')	