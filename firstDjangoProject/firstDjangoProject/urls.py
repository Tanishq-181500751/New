"""firstDjangoProject URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from firstDjangoProject import settings
from firstapp import views
urlpatterns = [
    path('',views.IndexPageController,name = "index_page"),
    path('firstPage',views.FirstPageController,name = "first_page"),

    path('htmlPages',views.HtmlPageController,name = "html_page"),

    path('htmlPagesWithData', views.HtmlPageControllerWithData, name="html_page_data"),

    path('htmlWithDataPass/<str:url_data>', views.PassingDataToController, name="html_data_pass"),

    path('admin/', admin.site.urls),
]
