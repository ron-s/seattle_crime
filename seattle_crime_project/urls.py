"""seattle_crime_project URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from seattle_crime_app import views as seattle_crime_app_views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'seattle_crime_app_crimemodel', seattle_crime_app_views.Crime2014DataViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', seattle_crime_app_views.home_page),
    url(r'^seattle_crime_app/', include(router.urls)),
]
