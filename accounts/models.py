# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser # Import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime 

# Your custom User model
class CustomUser(AbstractUser):    
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name=_("Phone Number"))
    admin_type = models.CharField(max_length=15, blank=True, null=True, verbose_name=_("Admin Type"))
    is_content_editor = models.BooleanField(default=False, verbose_name=_("Is Content Editor"))
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL' # Required when extending AbstractUser
        verbose_name = _("Custom User")
        verbose_name_plural = _("Custom Users")
        db_table = 'auth_user' 

    def __str__(self):
        return self.username
    
# main/models.py



# Helper function for image upload paths
def get_image_upload_path(instance, filename):
    return f'uploads/{instance.__class__.__name__.lower()}/{filename}'

# 7. Company Model (for global website settings/information)
class Company(models.Model):
   
    full_name = models.CharField(max_length=255, help_text="Full legal name of the company (e.g., Rovid Smart Technology).")
    short_name = models.CharField(max_length=50, blank=True, help_text="Short name or abbreviation (e.g., RovidGH).")
    logo = models.ImageField(upload_to=get_image_upload_path, blank=True, null=True, help_text="Company logo.")
    tagline = models.CharField(max_length=255, blank=True, help_text="A short, catchy phrase about the company.")
    mission = models.TextField(blank=True, help_text="Company mission statement.")
    vision = models.TextField(blank=True, help_text="Company vision statement.")
    values = models.JSONField(blank=True, help_text="Core values of the company.")
    about_us_text = models.TextField(blank=True, help_text="Longer 'About Us' section text.") # Renamed from 'about' to be more descriptive
    
    # Contact Information
    email = models.EmailField(blank=True, help_text="General contact email address.") # Added email as it's crucial
    location_description = models.CharField(max_length=255, blank=True, help_text="General location description (e.g., 'Accra, Ghana').") # Renamed from 'location' for clarity
    mailing_address = models.TextField(blank=True, help_text="Full mailing address.")
    postal_address = models.TextField(blank=True, help_text="Full postal address (if different from mailing).")
    tel = models.CharField(max_length=50, blank=True, help_text="Main telephone number.")
    fax = models.CharField(max_length=50, blank=True, help_text="Fax number.")
    phone1 = models.CharField(max_length=50, blank=True, help_text="Primary mobile/contact number.")
    phone2 = models.CharField(max_length=50, blank=True, help_text="Secondary mobile/contact number.")

    # Social Media Links
    linkedin = models.URLField(max_length=200, blank=True, null=True, help_text="LinkedIn profile URL.")
    x = models.URLField(max_length=200, blank=True, null=True, help_text="X (Twitter) profile URL.")
    facebook = models.URLField(max_length=200, blank=True, null=True, help_text="Facebook page URL.")
    instagram = models.URLField(max_length=200, blank=True, null=True, help_text="Instagram profile URL.") # Renamed from 'ig'
    tiktok = models.URLField(max_length=200, blank=True, null=True, help_text="TikTok profile URL.")
    youtube = models.URLField(max_length=200, blank=True, null=True, help_text="YouTube channel URL.")
    github = models.URLField(max_length=200, blank=True, null=True, help_text="GitHub profile/organization URL.")
    
    # Clarified Google and Yahoo usage - assuming they refer to business listings or general search profiles
    google_business_profile = models.URLField(max_length=200, blank=True, null=True, help_text="Google Business Profile URL (e.g., Google Maps listing).")
    yahoo_business_profile = models.URLField(max_length=200, blank=True, null=True, help_text="Yahoo Business Profile URL.")

    copyright_text = models.CharField(max_length=200, blank=True, help_text="Text for the website footer copyright (e.g., '© 2025 Rovid Smart Technology.').")

    class Meta:
        verbose_name_plural = "Company (Global Settings)"
       
        constraints = [
            models.UniqueConstraint(fields=['id'], name='unique_company_settings')
        ]

    def __str__(self):
        return f"{self.full_name} Settings"

