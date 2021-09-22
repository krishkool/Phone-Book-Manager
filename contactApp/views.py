from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactBook

#packages for login and logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
@login_required
def home(request):
    return render(request, 'index.html')

def addcontact(request):
    try:
        nameval    = request.POST['name']
        contactval = request.POST['contact']
        addval     = request.POST['address']
        
        # contactData = ContactBook.objects.all()
        contactData =  ContactBook.objects.get(Contact = contactval)

        if contactData is not None:
            return render(request, 'createcontact.html', {"failed": "Contact Number already exists"})
                        
    except Exception as e:
        print(e)
        addData = ContactBook(Name=nameval, Contact=contactval, Address=addval)
        addData.save()
        return render(request, 'createcontact.html', {"success": "Successfully Added!"})
        # return HttpResponse("Something Went Wrong in Creation!")

def createView(request):
    return render(request, 'createcontact.html')

def updateView(request):
    return render(request, 'updatecontact.html')

def displayView(request):
    return render(request, 'displaycontacts.html')

def deleteView(request):
    return render(request, 'deletecontact.html')

def deleteContact(request):
    try:
        contVal = request.POST['contact']
        nameVal = request.POST['name']

        contactData = ContactBook.objects.get(Contact = contVal, Name = nameVal)
        if contactData is not None:
            contactData.delete()
            return render(request, 'deletecontact.html', {"success": "Contact Deleted!"})
    except Exception as e:
        print(e)
        return render(request, 'deletecontact.html', {"failure": "Contact not exists!"})

def displayContact(request):
    try:
        conData = ContactBook.objects.all()
        return render(request, 'displaycontacts.html', {"data": conData})

    except Exception as e:
        print(e)
        return render(request, 'displaycontacts.html', {"failure": "Unable to display!"})

def updateName(request):
    try:
        conVal = request.POST['contact']
        current = request.POST['curname']
        new     = request.POST['newname']

        contactData = ContactBook.objects.get(Contact = conVal)
        contactData.Name = new
        contactData.save()
        return render(request, 'updatecontact.html', {"name": "Name Updated!"})
    except Exception as e:
        print(e)
        return render(request, 'updatecontact.html', {"name_failure": "Contact not exists!"})

def updateNumber(request):
    try:
        current = request.POST['curcontact']
        new = request.POST['newcontact']

        contactData = ContactBook.objects.get(Contact = current)
        contactData.Contact = new
        contactData.save()
        return render(request, 'updatecontact.html', {"number": "Number Updated!"})
    except Exception as e:
        print(e)
        return render(request, 'updatecontact.html', {"number_failure": "Contact not exists!"})

def updateAddress(request):
    try:
        conVal = request.POST['contact']
        current = request.POST['curaddress']
        new = request.POST['newaddress']

        contactData = ContactBook.objects.get(Contact = conVal)
        contactData.Address = new
        contactData.save()
        return render(request, 'updatecontact.html', {"address": "Address Updated!"})
    except Exception as e:
        print(e)
        return render(request, 'updatecontact.html', {"address_failure": "Contact not exists!"})

def login_view(request):
    uname = request.POST['username']
    pwd   = request.POST['password']

    user = authenticate(request, username = uname, password = pwd)

    if user is not None:
        login(request, user)
        return HttpResponse("Successfully Signed-Up!")
        return redirect('home')
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login')