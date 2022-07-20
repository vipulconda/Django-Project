from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import destination,Products
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):
	dests=destination.objects.all
	products=Products.objects.all
	form = ContactForm()
	return render(request,'index.html',{'dests' : dests,'products' : products, 'form':form})

    
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		print(form.is_valid())
		if form.is_valid():
			# subject = "Website Inquiry" 
			# body = {
			# 'first_name': form.cleaned_data['first_name'], 
			# 'last_name': form.cleaned_data['last_name'], 
			# 'email': form.cleaned_data['email_address'], 
			# 'message':form.cleaned_data['message'], 
			# }
			# message = "\n".join(body.values())

			# try:
			# 	is_send = send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			# except BadHeaderError:
			# 	return HttpResponse('Invalid header found.')
			f_name = form.cleaned_data['first_name']
			l_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email_address']
			mess = form.cleaned_data['message']
			print(f_name, l_name, email, mess)
			form.save()

			
      
	form = ContactForm()
	context = {}
	context['form'] = form
	context['message_abt_form'] = "Thank you for contacting us!!!"
	return render(request, "index.html", context)
    




  