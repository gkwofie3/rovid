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

# 1. Carousel Model
class Carousel(models.Model):
    title = models.CharField(max_length=100, help_text="Internal title for the carousel slide (e.g., 'Homepage Slide 1')", blank=True)
    image = models.ImageField(upload_to=get_image_upload_path, help_text="Background image for the carousel slide.")
    main_text = models.CharField(max_length=255, help_text="The primary headline or main message on the slide.")
    link = models.URLField(max_length=200, blank=True, null=True, help_text="Optional: URL this slide links to.")
    text_1 = models.TextField(blank=True, help_text="First line/paragraph of supporting text.") # Renamed from text_1c for clarity
    text_2 = models.TextField(blank=True, help_text="Second line/paragraph of supporting text.")
    icon = models.CharField(max_length=50, blank=True, help_text="Optional: FontAwesome icon class (e.g., 'fa fa-play').")
    order = models.IntegerField(default=0, help_text="Order in which the slides appear (lower number first).")
    is_active = models.BooleanField(default=True, help_text="Whether this slide is currently active on the website.")

    class Meta:
        verbose_name_plural = "Carousels"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title if self.title else f"Carousel Slide {self.id}"

# 2. Clients Model
class Client(models.Model):
   
    name = models.CharField(max_length=100, unique=True, help_text="Name of the client company or individual.")
    industry = models.CharField(max_length=100, blank=True, help_text="Industry of the client (e.g., 'Healthcare', 'Tech').")
    client_logo = models.ImageField(upload_to=get_image_upload_path, help_text="Logo of the client.")
    project_title = models.CharField(max_length=200, blank=True, help_text="Title of a specific project done for this client.")
    project_link = models.URLField(max_length=200, blank=True, null=True, help_text="Optional: Link to the detailed project page or case study.")
    display_on_homepage = models.BooleanField(default=False, help_text="Check to feature this client on the homepage.")

    class Meta:
        verbose_name_plural = "Clients"
        ordering = ['name']

    def __str__(self):
        return self.name

# 3. Services Model
class Service(models.Model):
    """
    Model for services offered by Rovid Smart Technology.
    """
    name = models.CharField(max_length=100, unique=True, help_text="Name of the service (e.g., 'Building Management Systems').")
    slug = models.SlugField(max_length=120, unique=True, blank=True,
                            help_text="Unique identifier for the service URL (auto-generated if left blank).")
    image = models.ImageField(upload_to=get_image_upload_path, help_text="Thumbnail or hero image for the service.")
    short_description = models.TextField(max_length=300, help_text="A brief summary for service listings.")
    details = models.TextField(help_text="Full, detailed description of the service.")
    category = models.CharField(max_length=100, help_text="Category of the service (e.g., 'Smart Infrastructure', 'Software Development').")
    link = models.URLField(max_length=200, blank=True, null=True, help_text="Optional: External URL if this service links elsewhere. Leave blank for internal dynamic links.")
    
    order = models.IntegerField(default=0, help_text="Order in which the service appears.")

    class Meta:
        verbose_name_plural = "Services"
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # This assumes you'll have a service_detail URL pattern that takes a slug
        return reverse('service_detail', kwargs={'slug': self.slug})


# 4. Testimony Model
class Testimony(models.Model):
    """
    Model for client testimonials or reviews.
    """
    person_name = models.CharField(max_length=100, help_text="Name of the person giving the testimony.")
    company_name = models.CharField(max_length=100, blank=True, help_text="Company name of the person giving the testimony.")
    title = models.CharField(max_length=100, blank=True, help_text="Job title or designation of the person.")
    client_role = models.CharField(max_length=100, blank=True, help_text="Their role related to your company (e.g., 'Client', 'Partner').")
    message = models.TextField(help_text="The actual testimony message.")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating out of 5 stars."
    )
    date_submitted = models.DateField(default=datetime.date.today, help_text="Date the testimony was given.")
    is_approved = models.BooleanField(default=False, help_text="Check to display this testimony on the website.")

    class Meta:
        verbose_name_plural = "Testimonies"
        ordering = ['-date_submitted', 'person_name']

    def __str__(self):
        return f"Testimony by {self.person_name} ({self.company_name})"
# 5. Contact Us Submission Model
class ContactMessage(models.Model):
    """
    Model to store submissions from the website's contact form.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, help_text="Subject of the message.")
    message = models.TextField()
    submission_time = models.DateTimeField(auto_now_add=True, help_text="Date and time when the message was submitted.")
    is_read = models.BooleanField(default=False, help_text="Mark as read after reviewing the message.")

    class Meta:
        verbose_name_plural = "Contact Messages"
        ordering = ['-submission_time']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

# 6. Projects Model
class Project(models.Model):
    """
    Model for individual projects completed by Rovid Smart Technology.
    """
    title = models.CharField(max_length=200, unique=True, help_text="Title of the project.")
    slug = models.SlugField(max_length=220, unique=True, blank=True,
                            help_text="Unique identifier for the project URL (auto-generated if left blank).")
    client_name = models.CharField(max_length=100, help_text="Name of the client for this project.")
    client_logo = models.ImageField(upload_to=get_image_upload_path, blank=True, null=True, help_text="Optional: Client's logo for this specific project.")
    description = models.TextField(help_text="Detailed description of the project, including scope and achievements.")
    category = models.CharField(max_length=100, help_text="Main category of the project (e.g., 'Smart Infrastructure', 'Software').")
    type = models.CharField(max_length=100, blank=True, help_text="Type of project (e.g., 'Residential', 'Commercial', 'Web Application').")
    location = models.CharField(max_length=200, blank=True, help_text="Geographical location of the project.")
    completion_date = models.DateField(help_text="Date the project was completed.")
    image1 = models.ImageField(upload_to=get_image_upload_path, blank=True, null=True, help_text="Main image for the project.")
    image2 = models.ImageField(upload_to=get_image_upload_path, blank=True, null=True, help_text="Second image for the project.")

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ['-completion_date', 'title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # This assumes you'll have a project_detail URL pattern that takes a slug
        return reverse('project_detail', kwargs={'slug': self.slug})

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

