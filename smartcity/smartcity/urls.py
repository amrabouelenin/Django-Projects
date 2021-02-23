"""smartcity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts import urls
import accounts, smartcity_app
from smartcity_app import urls
from smartcity_app import views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include(accounts.urls)),
    path('', RedirectView.as_view(url='login'), name='go-to-login'),
    path('', include(accounts.urls)),
    path('', include(smartcity_app.urls)),
    path('passenger/add/', include(accounts.urls)),
    path('beacons', include(smartcity_app.urls)),
    path('stationss', include(smartcity_app.urls)),
    path('trips', include(smartcity_app.urls)),
    path('dashboard',views.DashboardPage.as_view(), name = 'dashboard' )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
