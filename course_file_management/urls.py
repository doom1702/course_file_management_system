from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_login
from course_app import views as course_views
admin.site.site_header  =  "Course File Management System"  
admin.site.site_title  =  "Admin"
admin.site.index_title  =  "Admin Operations"
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', include("course_app.urls")),
    path('login/',auth_login.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_login.LogoutView.as_view(template_name='logout.html'),name='logout'),
    # path('profile/',course_views.profile,name='profile')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)