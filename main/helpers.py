from .models import *
from accounts.models import Company
"""Helper functions for main app.
admin.site.register(Service)
admin.site.register(Project)    
admin.site.register(BlogPost)
admin.site.register(JobPosting)
admin.site.register(ContactMessage)
admin.site.register(Testimony)
admin.site.register(Carousel)
admin.site.register(Client)
"""
def db(request):
    return {
        'name':"ROvid Smart...",
        'services': Service.objects.all(),
        'projects':Project.objects.all(),
        'blog_posts':BlogPost.objects.all(),
        'company':Company.objects.first(),
        'testimonies':Testimony.objects.all(),
        'carousels':Carousel.objects.all(),
        'clients':Client.objects.all(),
        'contact_messages':ContactMessage.objects.all(),

        
    }