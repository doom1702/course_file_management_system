from django.urls import path
from django.urls.conf import include
from django.contrib import admin
from . import views
from course_file_management import urls


urlpatterns = [
    path('',views.home,name="home"),
    path('admin',views.admin,name="admin"),
    path('vision',views.vision,name="vision"),
    path('depart',views.depart,name="depart"),
    path('ict',views.ict,name="ict"),
    path('qb',views.qb,name="qb"),
    path('rubrics',views.rubrics,name="rubrics"),
    path('uni_exam',views.uni_exam,name="uni_exam"),
    path('syllab',views.syllab,name="syllab"),
    path('delete_files/<int:pk>',views.delete_files,name='delete_files'),
    path('del_dep/<int:pk>',views.delete_dep,name='delete_dep'),
    path('delete_ict/<int:pk>',views.delete_ict,name='delete_ict'),
    path('delete_syllab/<int:pk>',views.delete_syllab,name='delete_syllab'),
    path('delete_uni_exam/<int:pk>',views.delete_uni_exam,name='delete_uni_exam'),
    path('delete_qb/<int:pk>',views.delete_qb,name='delete_qb'),
    path('delete_rubrics/<int:pk>',views.delete_rubrics,name='delete_rubrics'),
]
 