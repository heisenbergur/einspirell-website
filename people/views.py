from django.shortcuts import render
from .models import Person

def index(request):
	people = Person.objects
	return render(request,'people/index.html', {'people':people})

def team(request):
	people = Person.objects
	return render(request,'people/team.html', {'people':people})

def contact(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		number = request.POST['number']
		return render(request, 'people/contact.html', {'name':name})
	else:
		return render(request, 'people/contact.html')

def Demo(request):
	return render(request,'people/Demo.html')

def culture(request):
	return render(request,'people/culture.html')
