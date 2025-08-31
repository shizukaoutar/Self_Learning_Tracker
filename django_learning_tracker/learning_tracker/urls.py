from django.contrib import admin
from django.urls import path
from . import views
from .views import DetailProgramView, DetailCourseView, EditProgramView, DeleteProgramView, AddCourseView, AddSkillView, AddLearningGoalView, DeleteCourseView, AddProgramView, EditCourseView, DetailSkillView, DetailLearningGoalView, EditSkillView, EditLearningGoalView, DeleteSkillView, DeleteLearningGoalView    


urlpatterns = [
    #Listing all programs
    path('', views.list_programs, name='list_programs'),
    path('programs/', views.list_programs, name='list_programs'),

    #Listing detail program
    path('detail_program/<int:pk>/', DetailProgramView.as_view(), name='detail_program'),

    #Listing detail course
    path('detail_course/<int:pk>/', DetailCourseView.as_view(), name='detail_course'),

    #Listing detail skill
    path('detail_skill/<int:pk>/', DetailSkillView.as_view(), name='detail_skill'),

    #Listing detail Learning Goal
    path('detail_learning_goal/<int:pk>/', DetailLearningGoalView.as_view(), name='detail_learning_goal'),

    #Add program
    path('add_program/', AddProgramView.as_view(), name='add_program'),    

    #Add course
    path('detail_program/<int:program_id>/add_course/', AddCourseView.as_view(), name='add_course'),    

    #Add skill
    path('detail_program/<int:program_id>/add_skill/', AddSkillView.as_view(), name='add_skill'),    

    #Add learning goal
    path('detail_program/<int:program_id>/add_learning_goal/', AddLearningGoalView.as_view(), name='add_learning_goal'),    

    #Edit program
    path('edit_program/<int:pk>/edit/', EditProgramView.as_view(), name='edit_program'),    

    #Edit course
    path('edit_course/<int:pk>/edit/', EditCourseView.as_view(), name='edit_course'),    

    #Edit skill
    path('edit_skill/<int:pk>/', EditSkillView.as_view(), name='edit_skill'),        

    #Edit learning goal
    path('edit_learning_goal/<int:pk>/', EditLearningGoalView.as_view(), name='edit_learning_goal'),          

    #Delete program
    path('delete_program/<int:pk>/', DeleteProgramView.as_view(), name='delete_program'),               

    #Delete course
    path('delete_course/<int:pk>/', DeleteCourseView.as_view(), name='delete_course'),        

    #Delete skill
    path('delete_skill/<int:pk>/', DeleteSkillView.as_view(), name='delete_skill'),        

    #Delete learning goal
    path('delete_learning_goal/<int:pk>/', DeleteLearningGoalView.as_view(), name='delete_learning_goal'),                
    
]