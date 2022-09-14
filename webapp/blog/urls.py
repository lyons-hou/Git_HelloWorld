"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
#    path('main/', include('main.urls', namespace='main')),
    path('BiosUpload/', include('BiosUpload.urls', namespace='BiosUpload')),
    path('BiosDownload/', include('BiosDownload.urls', namespace='BiosDownload')),
    path('ReportUpload/', include('ReportUpload.urls', namespace='ReportUpload')),
    path('ReportDownload/', include('ReportDownload.urls', namespace='ReportDownload')),
    path('BiosLatestQuery/', include('BiosLatestQuery.urls', namespace='BiosLatestQuery')),
    path('BiosLatestQueryForMe/', include('BiosLatestQueryForMe.urls', namespace='BiosLatestQueryForMe')),
    path('BiosLatestQueryForUc/', include('BiosLatestQueryForUc.urls', namespace='BiosLatestQueryForUc')),    
    path('BiosLatestQueryForToken/', include('BiosLatestQueryForToken.urls', namespace='BiosLatestQueryForToken')),    
    path('BiosList/', include('BiosList.urls', namespace='BiosList')),
    path('SW_Inventory/', include('SW_Inventory.urls', namespace='SW_Inventory')),
    path('SW_InventoryDownload/', include('SW_InventoryDownload.urls', namespace='SW_InventoryDownload')),
] + static(settings.STATIC_URL, documnet_root=settings.STATIC_ROOT)
