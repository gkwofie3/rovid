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
