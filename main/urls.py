from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),

    # Individual Service Pages (as discussed)
    path('services/bms-solutions/', views.bms_solutions, name='bms_solutions'),
    path('services/cctv-installation/', views.cctv_installation, name='cctv_installation'),
    path('services/solar-installations/', views.solar_installations, name='solar_installations'),
    path('services/automatic-gates/', views.automatic_gates, name='automatic_gates'),
    path('services/web-app-development/', views.web_app_development, name='web_app_development'),
    path('services/mobile-desktop-app-development/', views.mobile_desktop_app_development, name='mobile_desktop_app_development'),
    path('services/industrial-automation/', views.industrial_automation, name='industrial_automation'),
    path('services/electrical-installation/', views.electrical_installation, name='electrical_installation'),
    path('services/smart-metering/', views.smart_metering, name='smart_metering'),
    path('services/graphic-design/', views.graphic_design, name='graphic_design'),
    path('services/video-production/', views.video_production, name='video_production'),
    path('services/3d-modeling/', views.three_d_modeling, name='3d_modeling'),

    # Other Utility Pages (as discussed)
    path('testimonials/', views.testimonials, name='testimonials'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
    path('faq/', views.faq, name='faq'),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)