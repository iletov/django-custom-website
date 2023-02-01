from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
	return render(request, 'index.html', {})

def contact(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		# company_name = request.POST['company']
		subject = request.POST['subject']
		message = request.POST['message']

		#send email
		send_mail(
    		name,
    		f'Subject: {subject}\n Phone: {phone}\n\n {message}',
    		email,
    		['letov88@gmail.com'],
    		fail_silently=False,
		)
		return render(request, 'contact.html', {'name':name})
	else:
		return render(request, 'contact.html', {})


def faq(request):
	return render(request, 'faq.html', {})

def about(request):
	return render(request, 'about.html', {})
