from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,auth

# from django.core.files.storage import FileSystemStorage

from django.contrib import messages

# from .forms import CreateUserForm


# import os
# from flask import Flask, request, url_for, send_from_directory
# from werkzeug import secure_filename
# import MySQLdb
# import glob

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

def input(request):
	return render(request,'input.html')	 

def upload(request):
	return render(request,'upload.html')	 	



# UPLOAD_FOLDER ="/tmp/"
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'csv'])
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def allowed_file(filename):
#   # this has changed from the original example because the original did not work for me
#     return filename[-3:].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             # print '**found file', file.filename
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

#         conn = MySQLdb.connect (host="localhost", port=3306, user="root",passwd=" ",db="mywebsite", local_infile = 1)
#         x = conn.cursor()
#         # print 'filename'
#         sql = """LOAD DATA LOCAL INFILE '{}'
#         INTO TABLE test
#         FIELDS TERMINATED BY ','
#         OPTIONALLY ENCLOSED BY '"'
#         LINES TERMINATED BY '\n'
#         IGNORE 1 LINES
#         """
#         os.chdir(UPLOAD_FOLDER)
#         dirfiles=glob.glob("*.csv")
#         for file_name in dirfiles:
#           # print file_name
#           if file_name==filename:
#             try:
#                 cursor = conn.cursor()
#                 file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#                 # print sql.format(file_path)
#                 cursor.execute(sql.format(file_path))
#                 conn.commit()
#                 # print "succses"
#             except Exception, e:
#                 # print e
#                 # Rollback in case there is any error
#                 conn.rollback()
#                 # for browser, add 'redirect' function on top of 'url_for'
#             return url_for('uploaded_file',
#                                     filename=filename)
#     return render(request, 'input.html') 

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)





