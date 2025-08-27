from django import forms
from .models import Program, Skill, Course, LearningGoal

#Program form
class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'

#Skill form
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

#Course form
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

#Learning Goal form
class LearningGoalForm(forms.ModelForm):
    class Meta:
        model = LearningGoal
        fields = '__all__'
