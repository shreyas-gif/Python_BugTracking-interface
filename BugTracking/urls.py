"""BugTracking URL Configuration

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
from django.urls import path
from bugapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login-user', login_user, name='login_user'),
    path('logout-user', logout_user, name='logout_user'),
    path('add-new-bug', add_new_bug, name='add_new_bug'),
    path('add-new-project', add_new_project, name='add_new_project'),
    path('add-new-user', add_new_user, name='add_new_user'),
    path('bug-report', bug_report, name='bug_report'),
    path('project-report', project_report, name='project_report'),
    path('user-report', user_report, name='user_report'),
    path('change-password', Change_Password, name='Change_Password'),
    path('profile', profile, name='profile'),
    path('edit-user/<int:pid>', edit_user, name='edit_user'),
    path('delete-user/<int:pid>', delete_user, name='delete_user'),
    path('edit-project/<int:pid>', edit_project, name='edit_project'),
    path('delete-project/<int:pid>', delete_project, name='delete_project'),
    path('edit-bug/<int:pid>', edit_bug, name='edit_bug'),
    path('delete-bug/<int:pid>', delete_bug, name='delete_bug'),
    path('bug-detail/<int:pid>', bug_detail, name='bug_detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
