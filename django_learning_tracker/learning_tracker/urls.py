from django.contrib import admin
from django.urls import path
from . import views
from .views import DetailProgramView, DetailCourseView, EditProgramView    


urlpatterns = [
    #Listing all programs
    path('', views.list_programs, name='list_programs'),
    path('programs/', views.list_programs, name='list_programs'),

    #Listing detail program
    path('detail_program/<int:pk>/', DetailProgramView.as_view(), name='detail_program'),

    #Listing all skills
    path('skills/', views.list_skills, name='list_skills'),

    #Listing all courses
    path('courses/', views.list_courses, name='list_courses'),

    #Listing detail course
    path('detail_course/<int:pk>/', DetailCourseView.as_view(), name='detail_course'),

    #Listing all learning goals
    path('learning_goals/', views.list_learning_goals, name='list_learning_goals'),

    #Add program
    path('add_program/', views.add_program, name='add_program'),    

    #Add skill
    path('add_skill/', views.add_skill, name='add_skill'),    

    #Add course
    path('add_course/', views.add_course, name='add_course'),    

    #Add learning goal
    path('add_learning_goal/', views.add_learning_goal, name='add_learning_goal'),    

    #Edit program
    path('edit_program/<int:pk>/edit/', EditProgramView.as_view(), name='edit_program'),        

    #Edit skill
    path('edit_skill/<int:pk>/', views.edit_skill, name='edit_skill'),        

    #Edit course
    path('edit_course/<int:pk>/', views.edit_course, name='edit_course'),        

    #Edit learning goal
    path('edit_learning_goal/<int:pk>/', views.edit_learning_goal, name='edit_learning_goal'),          

    #Delete program
    path('delete_program/<int:pk>/', views.delete_program, name='delete_program'),        

    #Delete skill
    path('delete_skill/<int:pk>/', views.delete_skill, name='delete_skill'),        

    #Delete course
    path('delete_course/<int:pk>/', views.delete_course, name='delete_course'),        

    #Delete learning goal
    path('delete_learning_goal/<int:pk>/', views.delete_learning_goal, name='delete_learning_goal'),                
    
]