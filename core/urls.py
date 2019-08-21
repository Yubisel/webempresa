from django.urls import path
from . import views as core_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('history/', core_views.history, name='history'),
    path('services/', core_views.services, name='services'),
    path('contact/', core_views.contact, name='contact'),
    path('visit_us/', core_views.visit_us, name='visit_us'),
    path('blog/', core_views.blog, name='blog'),
]