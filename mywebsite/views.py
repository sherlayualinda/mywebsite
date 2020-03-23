from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth

from django.core.files.storage import FileSystemStorage

from django.contrib import messages
from data.forms import DocumentForm
from data.models import Document

# from .forms import CreateUserForm




def registerPage(request):
	

	if request.method =='POST':
		first_name      = request.POST['first_name']
		last_name       = request.POST['last_name']
		username        = request.POST['username']
		email           = request.POST['email']
		password1       = request.POST['password1']
		password2       = request.POST['password2']

		if password1 == password2 :
			if User.objects.filter(username = username).exists():
				messages.info(request,'Username Taken')
				return redirect('register')
			elif User.objects.filter(email = email).exists():	
				messages.info(request,'Email Taken')
				return redirect('register')
			else:	
				user = User.objects.create_user(username= username, password=password1, email =email, first_name =first_name,last_name=last_name)
				user.save();
				print('user created')
				return redirect('login')
		else :
			messages.info(request,'Password not matching')
			return redirect('register')
		return redirect('/')
	else:	
		return render(request,'register.html')

     
def index(request):
    return render(request,'index.html')

def loginPage(request):
	if request.method=='POST':
		username        = request.POST['username']
		password        = request.POST['password']
		user = auth.authenticate(username = username, password = password)
		if user is not None :
			auth.login(request, user)
			return redirect("index")
		else:	
			 messages.info(request,'invalid creditials')
			 return redirect('login')
	else:
		return render(request,'login.html')

def logoutView(request):
	
	auth.logout(request)
	return render(request, 'login.html')	


def index(request):
	return render(request,'index.html')

def buttons(request):
	return render(request,'buttons.html')	

def history(request):
	return render(request,'history.html')	

def document_list(request):	
	documents = Document.objects.all()
	return render(request,'list.html',{
		'documents': documents
		})	 	

def upload(request):
	
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('document_list')
	else:
		form = DocumentForm()
	return render(request,'upload.html',{
		'form': form
		})

	 	


