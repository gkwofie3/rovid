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

from .models import Project, BlogPost, Service
from .helpers import db # Assuming db() is defined in a helpers.py file

# -----------------------------------------------------------
# PRIMARY NAVIGATION VIEWS
# -----------------------------------------------------------

def index(request):
    """Renders the main homepage content within main.html."""
    context = db(request)
    context['page_title'] = 'Building Management & Automation Solutions'
    context['html'] = 'index.html' 
    return render(request, 'main.html', context)

def about_view(request):
    """Renders the About Us page content within main.html."""
    context = db(request)
    context['page_title'] = 'About Us'
    # Fetch specific About Us data here (e.g., team members, history)
    context['html'] = 'rovid/about.html'
    return render(request, 'main.html', context)
def faq(request):
    """Renders the fa q Us page content within main.html."""
    context = db(request)
    context['page_title'] = 'Frequently Asked Questions'
    # Fetch specific fq Us data here (e.g., team members, history)
    context['html'] = 'rovid/faq.html'
    return render(request, 'main.html', context)

def contact_view(request):
    """Renders the Contact Us page content within main.html."""
    context = db(request)
    context['page_title'] = 'Contact Us'
    # Placeholder for form logic
    context['success'] = request.method == 'POST' # Simple success flag
    context['html'] = 'rovid/contact.html'
    return render(request, 'main.html', context)


def careers_view(request):
    """Renders the Careers page content within main.html."""
    context = db(request)
    context['page_title'] = 'Careers & Opportunities'
    # context['jobs'] = JobPosting.objects.filter(is_active=True)
    context['html'] = 'rovid/careers.html'
    return render(request, 'main.html', context)
def testimonials(request):
    context = db(request)
    context['page_title'] = 'Testimonials'
    # context['jobs'] = JobPosting.objects.filter(is_active=True)
    context['html'] = 'rovid/testimonials.html'
    return render(request, 'main.html', context)

# -----------------------------------------------------------
# PORTFOLIO / PROJECTS VIEWS
# -----------------------------------------------------------

def portfolio_view(request):
    """Renders the main Portfolio landing page content within main.html."""
    context = db(request)
    context['page_title'] = 'Our Portfolio'
    context['html'] = 'rovid/portfolio.html'
    return render(request, 'main.html', context)

def project_listing_view(request):
    """Renders the page that lists all available projects within main.html."""
    context = db(request)
    context['page_title'] = 'All Projects'
    # context['projects'] = Project.objects.all().order_by('-date')
    context['html'] = 'rovid/project.html'
    return render(request, 'main.html', context)

def project_detail_view(request, project_slug):
    """Renders a specific project case study within main.html."""
    # Assuming the project title comes from the slug
    dynamic_title = project_slug.replace('-', ' ').title()
    
    context = db(request)
    # project = get_object_or_404(Project, slug=project_slug)
    context['slug'] = project_slug
    context['title'] = dynamic_title # Used for the main heading on the page
    context['page_title'] = f'Project: {dynamic_title}' # Used for the HTML <title>
    context['html'] = 'rovid/project_detail.html'
    return render(request, 'main.html', context)


# -----------------------------------------------------------
# BLOG / INSIGHTS VIEWS
# -----------------------------------------------------------

def blog_listing_view(request):
    """Renders the page that lists all blog posts within main.html."""
    context = db(request)
    context['page_title'] = 'Insights & Blog'
    # context['posts'] = BlogPost.objects.filter(published=True).order_by('-date')
    context['html'] = 'rovid/blog.html'
    return render(request, 'main.html', context)


def blog_post_view(request, post_slug):
    """Renders a single, detailed blog post within main.html."""
    # Assuming the post title comes from the slug
    dynamic_title = post_slug.replace('-', ' ').title()

    context = db(request)
    # post = get_object_or_404(BlogPost, slug=post_slug)
    context['slug'] = post_slug
    context['title'] = dynamic_title # Used for the main heading on the page
    context['page_title'] = f'Insight: {dynamic_title}' # Used for the HTML <title>
    context['html'] = 'rovid/blog_post.html'
    return render(request, 'main.html', context)


# -----------------------------------------------------------
# SERVICE DETAIL VIEW
# -----------------------------------------------------------

def service_detail_view(request, service_slug):
    """Renders a specific service detail page within main.html."""
    # Assuming the service title comes from the slug
    dynamic_title = service_slug.replace('-', ' ').title()
    
    context = db(request)
    # service = get_object_or_404(Service, slug=service_slug)
    context['slug'] = service_slug
    context['title'] = dynamic_title # Used for the main heading on the page
    context['page_title'] = f'Service: {dynamic_title}' # Used for the HTML <title>
    context['html'] = 'rovid/service_detail.html'
    return render(request, 'main.html', context)


# -----------------------------------------------------------
# FOOTER LEGAL VIEWS (Static Content)
# -----------------------------------------------------------

def privacy_policy_view(request):
    """Renders the Privacy Policy page content within main.html."""
    context = db(request)
    context['page_title'] = 'Privacy Policy'
    context['html'] = 'rovid/privacy_policy.html'
    return render(request, 'main.html', context)

def terms_of_service_view(request):
    """Renders the Terms of Service page content within main.html."""
    context = db(request)
    context['page_title'] = 'Terms of Service'
    context['html'] = 'rovid/terms_of_service.html'
    return render(request, 'main.html', context)