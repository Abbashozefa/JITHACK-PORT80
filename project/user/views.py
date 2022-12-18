

# Create your views here.
from django.shortcuts import render,redirect

from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from .models import ContactForm,ServiceForm



import requests

# Create your views here.
def landing(request):
	return render(request, 'landing.html')
def contact(request):
	if (request.method == 'POST'):
		fullname=request.POST.get('fullname')
		email=request.POST.get('email')
		contact=request.POST.get('contact')
		message=request.POST.get('message')
		contact=ContactForm(fullname=fullname,email=email,contact=contact,message=message)
		contact.save()
		
	return render(request, 'Contact.html')
def services(request):
	if (request.method == 'POST'):
		post=ServiceForm
		post.cname=request.POST['cname']
		post.cemail=request.POST['cemail']
		post.ccontact=request.POST['ccontact']
		post.cdate=request.POST['cdate']
		post.clocation=request.POST['clocation']
		post.cservice=request.POST['cservice']				
		post.save()
		return render(request, 'services.html')
	else:
		return render(request, 'services.html')
	
	return render(request, 'services.html')
def about(request):
	return render(request, 'About.html')
def donation(request):
	return render(request,'donation.html')
def serviceform(request):	 
    #if request.method == "POST":  
    #    fullname=  
    return render(request,'forms.html')

#def emp(request):  
#    if request.method == "POST":  
#        form = EmployeeForm(request.POST)  
#        if form.is_valid():  
#            try:  
#                form.save()  
#                return redirect('/show')  
#            except:  
#                pass  
#    else:  
#        form = EmployeeForm()  
#    return render(request,'index.html',{'form':form})  
#def show(request):
#    
#    
#      
#    employees = Employee.objects.all() 
#        
#      
#            
#    return render(request,"show.html",{'employees':employees})     
#def edit(request, id):  
#    employee = Employee.objects.get(id=id)  
#    return render(request,'edit.html', {'employee':employee})  
#def update(request, id):  
#    employee = Employee.objects.get(id=id)  
#    form = EmployeeForm(request.POST, instance = employee)  
#    if form.is_valid():  
#        form.save()  
#        return redirect("/show")  
#    return render(request, 'edit.html', {'employee': employee})  
#def destroy(request, id):  
#    employee = Employee.objects.get(id=id)  
#    employee.delete()  
#    return redirect("/show")
#


#index
def index(request):
	return render(request, 'user/index.html', {'title':'index'})

#register here
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			# mail system 
			htmly = get_template('user/Email.html')
			d = { 'username': username }
			subject, from_email, to = 'welcome', 'hozefaabbas1911@gmail.com', email
			html_content = htmly.render(d)
			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
			msg.attach_alternative(html_content, "text/html")
			msg.send()
			##################################################################
			messages.success(request, f'Your account has been created ! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'user/register.html', {'form': form, 'title':'register here'})

################ login forms###################################################
def Login(request):
	if request.method == 'POST':

		# AuthenticationForm_can_also_be_used__

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username, password = password)
		if user is not None:
			form = login(request, user)
			messages.success(request, f' welcome {username} !!')
			return redirect('index')
		else:
			messages.info(request, f'account done not exit plz sign in')
	form = AuthenticationForm()
	return render(request, 'user/login.html', {'form':form, 'title':'log in'})
