

from django.db import models
from django.contrib.auth.models import AbstractUser # Import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime 
# -----------------------------------------------------------
# CORE SITE MODELS
# -----------------------------------------------------------
def get_image_upload_path(instance, filename):
    return f'uploads/{instance.__class__.__name__.lower()}/{filename}'

class Service(models.Model):
    """Represents a specific service offered (e.g., Building Management Systems)."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="A URL-friendly short label.")
    summary = models.TextField(max_length=500)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="e.g., bi bi-building-gear")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    """Represents an article or insight on the company blog."""
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100)
    publish_date = models.DateField(auto_now_add=True)
    content = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class JobPosting(models.Model):
    """Represents a career opportunity or job listing."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    is_active = models.BooleanField(default=True)
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

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
    service_of_interest= models.CharField(max_length=100, blank=True, help_text="Optional: Service the sender is interested in.")   
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
