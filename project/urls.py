"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),  # Create a new path for the home page
    path("accounts/", include("accounts.urls")),  # It is very important to include this BEFORE the built-in authentication URLs
    path("accounts/", include("django.contrib.auth.urls")),  # Add the path for the built-in authentication URLs
    path("plane/", TemplateView.as_view(template_name="transport/plane.html"), name="plane"),
    path("subway/", TemplateView.as_view(template_name="transport/subway.html"), name="subway"),
    path("car/", TemplateView.as_view(template_name="transport/car.html"), name="car"),
    path("boat/", TemplateView.as_view(template_name="transport/boat.html"), name="boat"),
    path("train/", TemplateView.as_view(template_name="transport/train.html"), name="train"),
    path("motorbike/", TemplateView.as_view(template_name="transport/motorbike.html"), name="motorbike"),
    path("calculate/", TemplateView.as_view(template_name="calculate.html"), name="calculate"),
    path("resultcar/", TemplateView.as_view(template_name="resultcar.html"), name="resultcar"),
    path("resultboat/", TemplateView.as_view(template_name="resultboat.html"), name="resultBoat"),
    path("resultmotorbike/", TemplateView.as_view(template_name="resultmotorbike.html"), name="resultMotorbike"),
    path("resultsubway/", TemplateView.as_view(template_name="resultsubway.html"), name="resultSubway"),
    path("resulttrain/", TemplateView.as_view(template_name="resulttrain.html"), name="resultTrain"),
    path('error/', TemplateView.as_view(template_name="error.html"), name='error_page'),
    path('results/', TemplateView.as_view(template_name="results.html"), name='results'),
    path('results/edit/', TemplateView.as_view(template_name="edit_result.html"), name='edit_result'),
    path('results/delete/', TemplateView.as_view(template_name="confirm_delete.html"), name='confirm_delete')
]
