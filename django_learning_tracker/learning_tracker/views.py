from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Program, Skill, Course, LearningGoal
from django.views.generic.detail import DetailView
from .forms import ProgramForm, SkillForm, CourseForm, LearningGoalForm
from django.views.generic import UpdateView, CreateView, DeleteView


# Create your views here.

### Listing items ###

#Listing all programs
def list_programs(request):
    programs = Program.objects.all()
    context = {'programs': programs}
    return render(request, 'learning_tracker/list_programs.html', context)

class DetailProgramView(DetailView):
    model = Program
    template_name = 'learning_tracker/detail_program.html' 

    
#Listing all skills
def list_skills(request):
    skills = Skill.objects.all()
    context = {'skills': skills}
    return render(request, 'learning_tracker/list_skills.html', context)
    
#Listing all courses
def list_courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'learning_tracker/list_courses.html', context)

class DetailCourseView(DetailView):
    model = Course
    template_name = 'learning_tracker/detail_course.html'
    
    
#Listing all learning goals
def list_learning_goals(request):
    learning_goals = LearningGoal.objects.all()
    context = {'learning_goals': learning_goals}
    return render(request, 'learning_tracker/list_learning_goals.html', context)
    

### Adding items ###

#Add program
class AddProgramView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'learning_tracker/add_program.html'
    success_url = reverse_lazy('list_programs')


#Add skill
def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_skills')
    else:
        form = SkillForm()
    
    context = {'form': form}
    return render(request, 'learning_tracker/add_skill.html', context)


#Add course
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        program = request.POST.get('program')
        if form.is_valid():
            form.save()
            return redirect('list_courses')
    else:
        form = CourseForm()
    
    context = {'form': form}
    return render(request, 'learning_tracker/add_course.html', context)


#Add learning goal
def add_learning_goal(request):
    if request.method == 'POST':
        form = LearningGoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_learning_goals')
    else:
        form = LearningGoalForm()
    
    context = {'form': form}
    return render(request, 'learning_tracker/add_learning_goal.html', context)


### Editing items ###

#Edit program
class EditProgramView(UpdateView):
    model = Program
    form_class = ProgramForm
    queryset = Program.objects.all()
    template_name = 'learning_tracker/edit_program.html'
   
    def get_success_url(self):
        return reverse('detail_program', kwargs={'pk': self.kwargs['pk']})

    def get_object(self):
        id = self.kwargs.get('pk')
        return get_object_or_404(Program, pk=id)
    

#Edit skill
def edit_skill(request, pk):
    skill = Skill.objects.get(pk=pk)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('list_skills')
    else:
        form = SkillForm(instance=skill)
    
    context = {'form': form}
    return render(request, 'learning_tracker/edit_skill.html', context)

#Edit course
def edit_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('list_courses')
    else:
        form = CourseForm(instance=course)
    
    context = {'form': form}
    return render(request, 'learning_tracker/edit_course.html', context)

#Edit learning goal
def edit_learning_goal(request, pk):
    learning_goal = LearningGoal.objects.get(pk=pk)
    if request.method == 'POST':
        form = LearningGoalForm(request.POST, instance=learning_goal)
        if form.is_valid():
            form.save()
            return redirect('list_learning_goals')
    else:
        form = LearningGoalForm(instance=learning_goal)
    
    context = {'form': form}
    return render(request, 'learning_tracker/edit_learning_goal.html', context)


### Deleting items ###

#Delete program
class DeleteProgramView(DeleteView):
    model = Program
    template_name = 'learning_tracker/delete_program.html'
    success_url = reverse_lazy('list_programs')

    def get_object(self):
        id = self.kwargs.get('pk')
        return get_object_or_404(Program, pk=id)

    def get_success_url(self):
        return reverse('list_programs')

#Delete skill
def delete_skill(request, pk):
    skill = Skill.objects.get(pk=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('list_skills')

#Delete course
def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('list_courses')

#Delete learning goal
def delete_learning_goal(request, pk):
    learning_goal = LearningGoal.objects.get(pk=pk)
    if request.method == 'POST':
        learning_goal.delete()
        return redirect('list_learning_goals')


