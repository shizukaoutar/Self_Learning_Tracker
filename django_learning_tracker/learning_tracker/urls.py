



urlpatterns = [
    #Listing all programs
    path('', views.list_programs, name='list_programs'),
    path('programs/', views.list_programs, name='list_programs'),

    #Listing all skills
    path('skills/', views.list_skills, name='list_skills'),

    #Listing all courses
    path('courses/', views.list_courses, name='list_courses'),

    #Listing all learning goals
    path('learning_goals/', views.list_learning_goals, name='list_learning_goals'),


    
]