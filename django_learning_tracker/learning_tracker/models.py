from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Program(models.Model):
    STATUS_CHOICES = [
        ('PLANNED', 'Planned'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('PAUSED', 'Paused'),
        ('DROPPED', 'Dropped'),
    ]
    
    DIFFICULTY_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    provider = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLANNED')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    progress_percentage = models.IntegerField(default=0)
    program_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name    

    def get_absolute_url(self):
        return reverse('detail_program', kwargs={'pk': self.pk})

class Course(models.Model):
    STATUS_CHOICES = [
        ('PLANNED', 'Planned'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('PAUSED', 'Paused'),
        ('DROPPED', 'Dropped'),
    ]
    
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration_hours = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLANNED')
    start_date = models.DateField(null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    progress_percentage = models.IntegerField(default=0)
    course_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Skill(models.Model):
    SKILL_LEVEL_CHOICES = [
        ('BEGINNER', 'Beginner'),
        ('INTERMEDIATE', 'Intermediate'),
        ('ADVANCED', 'Advanced'),
        ('EXPERT', 'Expert'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVEL_CHOICES)
    
    def __str__(self):
        return self.name    


class ProgramSkill(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='program_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='program_skills')
    
    class Meta:
        unique_together = ('program', 'skill')
    
    def __str__(self):
        return f"{self.program.name} - {self.skill.name}"


class LearningGoal(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    target_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='MEDIUM')
    is_achieved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class ProgramGoal(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='program_goals')
    learning_goal = models.ForeignKey(LearningGoal, on_delete=models.CASCADE, related_name='program_goals')
    
    class Meta:
        unique_together = ('program', 'learning_goal')
    
    def __str__(self):
        return f"{self.program.name} - {self.learning_goal.title}"