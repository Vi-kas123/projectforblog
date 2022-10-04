"""Blogwebsite URL Configuration

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
from django.urls import path
from . import AdminRegistrationController
from . import AdminLoginController
from . import BlogPostController
from . import UserInterfaceController
urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminregistration/',AdminRegistrationController.Admin_Registration),
    path('adminrecordsubmit',AdminRegistrationController.SubmitAdminData),
    path('adminlogin/',AdminLoginController.Login_Interface),
    path('admincheck', AdminLoginController.Check_Admin),
    path('addblog',BlogPostController.AddBlog),
    path('submitblog', BlogPostController.Submit_Blog),
    path('adminlogout/', AdminLoginController.Admin_Logout),
    path('displayblog', BlogPostController.Display_All_Blog),
    path('editblog', BlogPostController.Edit_Blog),
    path('deleteblog', BlogPostController.Delete_Blog),
    path('userinterface',UserInterfaceController.User_Index),
    path('fetch_all_blogs', UserInterfaceController.Fetch_All_blogs),
    path('blog_description', UserInterfaceController.BlogDescription),

]
