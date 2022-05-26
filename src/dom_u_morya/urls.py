"""dom_u_morya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from houses.views import houses_list, house_detail, HousesAPIListView, HousesAPIDestroyView, HousesAPIUpdateView
#HousesViewSet, HousesAPIDetailView,  #HousesAPIUpdate

from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers



urlpatterns = [
    path('', houses_list, name='home'),
    path('<int:house_id>/', house_detail, name='house'),
    path('api/v1/houseslist/', HousesAPIListView.as_view()),
#    path('api/v1/houseslist/<int:pk>/', HousesViewSet.as_view({'put': 'update'})),
    #path('api/v1/housedetail/<int:pk>/', HousesAPIDetailView.as_view()),
    path('api/v1/houseupdate/<int:pk>/', HousesAPIUpdateView.as_view()),
    path('api/v1/housedelete/<int:pk>/', HousesAPIDestroyView.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
