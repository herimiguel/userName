from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


# Create your views here.

def index(request):    
    return render(request, 'my_app/index.html')

def submit_user(request):
    isValid = True
    if request.method == 'POST':
        minVal= 4
        maxVal = 15
        
    if len(request.POST['user_name']) < minVal:
        messages.error(request, 'should not be less than 8 characters!')
        isValid = False

    if len(request.POST['user_name']) >maxVal:
        # messages.add_message(request, messages.ERROR, 'should not be more than 15 characters!')
        messages.error(request, 'should not be more than 15 characters!')
        isValid = False
    if not isValid:   
        return redirect('/')
        
    else:
        User.objects.create(user_name = request.POST['user_name'])
        print "created a user"
        # return render (request,'my_app/success.html')
        return redirect('/success')
         
def success(request):
    context={
        'users': User.objects.all()
    }
    return render(request, 'my_app/success.html', context)

def delete_user(request, id):
    User.objects.get(id=id).delete()
    
    return redirect('/success')  