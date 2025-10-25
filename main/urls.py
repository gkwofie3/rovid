from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Home page

    # Other Utility Pages (as discussed)
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('careers/', views.careers_view, name='careers'),
    
    # -------------------
    # PORTFOLIO/PROJECTS
    # - /portfolio/ is the main landing page
    # - /portfolio/projects/ is the list of all projects
    # - /projects/slug/ is the detail page (keeping your original link structure for projects)
    # -------------------
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('portfolio/projects/', views.project_listing_view, name='project_listing'),
    path('projects/<slug:project_slug>/', views.project_detail_view, name='project_detail'),

    # -------------------
    # BLOG/INSIGHTS
    # - /blog/ is the listing page (shows list of all posts)
    # - /blog/post-title/ is the detail page for a single post
    # -------------------
    path('blog/', views.blog_listing_view, name='blog_listing'), # Renamed for clarity
    path('blog/<slug:post_slug>/', views.blog_post_view, name='blog_post_detail'), 

    # -------------------
    # SERVICE DETAIL PAGES (Generic URL)
    # -------------------
    path('services/<slug:service_slug>/', views.service_detail_view, name='service_detail'),

    # -------------------
    # FOOTER LEGAL LINKS
    # -------------------
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service_view, name='terms_of_service'),
    path('testimonials/', views.testimonials, name='testimonials'),

    path('faq/', views.faq, name='faq'),
]
# core/urls.py

from django.urls import path
from . import views

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)