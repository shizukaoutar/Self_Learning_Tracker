from django.db import models

# Create your models here.

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    provider = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    progress_percentage = models.IntegerField(default=0)
    program_url = models.URLField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name    



class Course(models.Model):
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration_hours = models.IntegerField()
    status = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    completion_date = models.DateField()
    progress_percentage = models.IntegerField(default=0)
    course_url = models.URLField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name



class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    skill_level = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name    


class ProgramSkill(models.Model):
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.program_id.name + " - " + self.skill_id.name



class LearningGoal(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    target_date = models.DateField()
    priority = models.CharField(max_length=100)
    is_achieved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class ProgramGoal(models.Model):
    program_id = models.ForeignKey(Program, on_delete=models.CASCADE)
    learning_goal_id = models.ForeignKey(LearningGoal, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.program_id.name + " - " + self.learning_goal_id.name
    

