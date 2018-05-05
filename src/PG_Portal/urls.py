"""PG_Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from app.views import (login_view, register_view, logout_view, 
    booking_view, booking_success, contact_us, 
    review_create, booking_detail, check_availibility, 
    gallery, booking_detail, about, 
    blog, faq, room_detail, room_detail1, 
    room_detail2, room_detail3, payment_view)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('app.urls', namespace='app')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^check_availibility/', check_availibility, name='check_availibility'),
    url(r'^booking/', booking_view, name='booking'),
    url(r'^contact_us/', contact_us, name='contact_us'),
    url(r'^review_create/', review_create, name='review_create'),
    url(r'^checkout/', payment_view, name='checkout'),
    url(r'^booking_success/', booking_success, name='booking_success'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^gallery/', gallery, name='gallery'),
    url(r'^booking_detail/', booking_detail, name='booking_detail'),
    url(r'^about/', about, name='about'),
    url(r'^blog/', blog, name='blog'),
    url(r'^faq/', faq, name='faq'),
    url(r'^room_detail/', room_detail, name='room_detail'),
    url(r'^room_detail1/', room_detail1, name='room_detail1'),
    url(r'^room_detail2/', room_detail2, name='room_detail2'),
    url(r'^room_detail3/', room_detail3, name='room_detail3'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
