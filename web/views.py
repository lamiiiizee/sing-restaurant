import json
from django.shortcuts import render

from web.models import Menu
from web.models import Branch
from web.models import Review
from web.models import Gallery
from web.models import CarouselSlide


from .forms import ContactForm

from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
import json
import random

from django.http import HttpResponse



# Create your views here.


def contact(request):
    branch=Branch.objects.all()
    # Create an instance of the ContactForm, either with POST data or None
    form = ContactForm(request.POST or None)
    
    if request.method == "POST":
        # If the request method is POST, check if the form data is valid
        if form.is_valid():
            # If the form data is valid, save it to the database
            form.save()
            # Create a JSON response indicating success
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            # If the form data is not valid, create a JSON response indicating failure
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": "Please correct the errors below and try again.",
            }
        
        # Return a JSON response with the appropriate message
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        # If the request method is not POST, render the contact form template with the ContactForm instance
        context = {
            "is_contact": True,
            "form": form,
            "branch":branch
        }
        return render(request, "web/contact.html", context)



def index(request):
    review=Review.objects.all()
    menu=Menu.objects.all()
    carousel_data = CarouselSlide.objects.all()



    context={"review":review,"menu":menu,'carousel_data': carousel_data}
    return render(request, 'web/index.html', context)

def about(request):
    review=Review.objects.all()
    context={"review":review}
    return render(request,'web/about.html',context)

def menu(request):
    menu=Menu.objects.all()
    context={"menu":menu}
    return render(request,'web/menu.html',context)





def branch(request):
    branch=Branch.objects.all()
    context={"branch":branch}
    return render(request,'web/branch.html',context)



def single_branch(request,id):
    branch=Branch.objects.get(id=id)
    branches=Branch.objects.all()
    context = {"branch": branch, "branches": branches}
    return render(request,'web/branch-single2.html',context)


def gallery(request):
    gallery=Gallery.objects.all().order_by('?')
    context={"gallery":gallery}
    return render(request,'web/gallery.html',context)

