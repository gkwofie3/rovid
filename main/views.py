# Create your views here.
from django.shortcuts import render,redirect
from django.utils import timezone
import pytz
from django.http import HttpResponse,JsonResponse
from urllib import request, response
from django.contrib import messages
# from .models import
import random
import string
from io import BytesIO
import re
import os
from collections import defaultdict
from django.conf import settings
from django.shortcuts import get_object_or_404
from datetime import datetime,timedelta,date
from django.apps import apps
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.models import Q

from django.utils.timezone import now

context={}
def index(request): # Initialize context for each view
    context['page_title'] = 'Home - Rovid Smart Technology'
    return render(request, 'main/index.html', context)

def about(request):
    context['page_title'] = 'About Us - Rovid Smart Technology'
    return render(request, 'main/about.html', context) 

def blog(request):
    context['page_title'] = 'Blog - Rovid Smart Technology'
    return render(request, 'main/blog.html', context)

def services(request):
    context['page_title'] = 'Our Services - Rovid Smart Technology'
    return render(request, 'main/services.html', context) 

def projects(request):
    context['page_title'] = 'Projects - Rovid Smart Technology'
    return render(request, 'main/projects.html', context) 

def contact(request):
    context['page_title'] = 'Contact Us - Rovid Smart Technology'
    return render(request, 'main/contact.html', context)

# --- Individual Service Views ---

def bms_solutions(request):
    context['page_title'] = 'BMS Solutions - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

def cctv_installation(request):
    context['page_title'] = 'CCTV Installation - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

def solar_installations(request):
    context['page_title'] = 'Solar Installations - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

def automatic_gates(request):
    context['page_title'] = 'Automatic Gates - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

def web_app_development(request):
    context['page_title'] = 'Web App Development - Rovid Smart Technology'
    return render(request, 'main/empty.html', context)

def mobile_desktop_app_development(request):
    context['page_title'] = 'Mobile & Desktop App Development - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

def industrial_automation(request):
    context['page_title'] = 'Industrial Automation - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

def electrical_installation(request):
    context['page_title'] = 'Electrical Installation - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

def smart_metering(request):
    context['page_title'] = 'Smart Metering - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

def graphic_design(request):
    context['page_title'] = 'Graphic Design - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

def video_production(request):
    context['page_title'] = 'Video Production - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

def three_d_modeling(request): 
    context['page_title'] = '3D Modeling - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

# --- Other Utility Views ---


def testimonials(request):
    context['page_title'] = 'Testimonials - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 
def portfolio(request):
    context['page_title'] = 'Portfolio - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 
def privacy_policy(request):
    context['page_title'] = 'Privacy Policy - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 

def terms_conditions(request):
    context['page_title'] = 'Terms & Conditions - Rovid Smart Technology'
    return render(request, 'main/empty.html', context)

def faq(request):
    context['page_title'] = 'FAQ - Rovid Smart Technology'
    return render(request, 'main/empty.html', context) 