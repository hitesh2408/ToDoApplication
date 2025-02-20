"""
URL configuration for toDoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from toDoApp.views import about, index, ToDoTasksView

admin.site.site_header = "Utilities Application Admin"
admin.site.site_title = "Utilities Application Admin Portal"
admin.site.index_title = "Welcome to Utilities Application Portal"

handler404 = 'base.views.custom_404_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all_tasks/', ToDoTasksView.as_view()),
    path('', index),
    path('about/', about),
    path('base/', include('base.urls'))
]
