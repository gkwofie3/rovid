from django.db import models

# -----------------------------------------------------------
# CORE SITE MODELS
# -----------------------------------------------------------

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

class Project(models.Model):
    """Represents a client case study or completed work."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    client = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    completion_date = models.DateField()
    summary = models.TextField(max_length=500)
    challenge_solution = models.TextField(help_text="Detailed project breakdown.")
    image = models.ImageField(upload_to='projects/', null=True, blank=True)

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

# -----------------------------------------------------------
# Your requested 'db' function is not standard for models.py, 
# so it is not included here. See the revised views.py below.
# -----------------------------------------------------------