from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Program, Skill, Course, LearningGoal, ProgramSkill, ProgramGoal
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

#Listing program detail
class DetailProgramView(DetailView):
    model = Program
    template_name = 'learning_tracker/detail_program.html' 

#Listing course detail
class DetailCourseView(DetailView):
    model = Course
    template_name = 'learning_tracker/detail_course.html'

#Listing skill detail
class DetailSkillView(DetailView):
    model = ProgramSkill
    template_name = 'learning_tracker/detail_skill.html'
    context_object_name = 'program_skill'

#Listing learning goal detail
class DetailLearningGoalView(DetailView):
    model = ProgramGoal
    template_name = 'learning_tracker/detail_learning_goal.html'
    context_object_name = 'program_goal'

### Adding items ###

#Add program
class AddProgramView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'learning_tracker/add_program.html'
    success_url = reverse_lazy('list_programs')

#Add course
class AddCourseView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'learning_tracker/add_course.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['program_id'] = self.kwargs.get('program_id')
        return context

    def get_success_url(self):
        program_id = self.kwargs.get('program_id')
        return reverse('detail_program', kwargs={'pk': program_id})

    def form_valid(self, form):
        program_id = self.kwargs.get('program_id')
        if program_id:
            program = get_object_or_404(Program, pk=program_id)
            form.instance.program = program
        return super().form_valid(form)

#Add skill
class AddSkillView(CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'learning_tracker/add_skill.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['program_id'] = self.kwargs.get('program_id')
        return context

    def get_success_url(self):
        program_id = self.kwargs.get('program_id')
        return reverse('detail_program', kwargs={'pk': program_id})

    def form_valid(self, form):
        # Save the skill
        response = super().form_valid(form)
        # Get the program and create ProgramSkill relationship
        program_id = self.kwargs.get('program_id')
        if program_id:
            program = get_object_or_404(Program, pk=program_id)
            ProgramSkill.objects.create(program=program, skill=form.instance)

        return response


#Add learning goal
class AddLearningGoalView(CreateView):
    model = LearningGoal
    form_class = LearningGoalForm
    template_name = 'learning_tracker/add_learning_goal.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['program_id'] = self.kwargs.get('program_id')
        return context

    def get_success_url(self):
        program_id = self.kwargs.get('program_id')
        return reverse('detail_program', kwargs={'pk': program_id})

    def form_valid(self, form):
        response = super().form_valid(form)
        program_id = self.kwargs.get('program_id')
        if program_id:
            program = get_object_or_404(Program, pk=program_id)
            ProgramGoal.objects.create(program=program, learning_goal=form.instance)

        return response


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
    
#Edit course
class EditCourseView(UpdateView):
    model = Course
    form_class = CourseForm
    queryset = Course.objects.all()
    template_name = 'learning_tracker/edit_course.html'
   
    def get_success_url(self):
        return reverse('detail_course', kwargs={'pk': self.kwargs['pk']})

    def get_object(self):
        id = self.kwargs.get('pk')
        return get_object_or_404(Course, pk=id)

#Edit skill
class EditSkillView(UpdateView):
    model = ProgramSkill 
    template_name = 'learning_tracker/edit_skill.html'
    fields = []

    def get_form(self, form_class=None):
        # Create a form for the underlying Skill object
        return SkillForm(data=self.request.POST or None, instance=self.object.skill)
    
    def form_valid(self, form):
        # Save the Skill object
        form.save()
        return redirect('detail_skill', pk=self.object.pk)

    def get_success_url(self):
        return reverse('detail_program', kwargs={'pk': self.object.program.pk})

#Edit learning goal
class EditLearningGoalView(UpdateView):
    model = ProgramGoal
    template_name = 'learning_tracker/edit_learning_goal.html'
    fields = []

    def get_form(self, form_class=None):
        # Create a form for the underlying LearningGoal object
        return LearningGoalForm(data=self.request.POST or None, instance=self.object.learning_goal)
    
    def form_valid(self, form):
        # Save the LearningGoal object
        form.save()
        return redirect('detail_learning_goal', pk=self.object.pk)

    def get_success_url(self):
        return reverse('detail_program', kwargs={'pk': self.object.program.pk})


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

#Delete course
class DeleteCourseView(DeleteView):
    model = Course
    template_name = 'learning_tracker/delete_course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['program_id'] = self.object.program.id
        return context

    def get_success_url(self):
        return reverse('detail_program', kwargs={'pk': self.object.program.id})
    

#Delete skill
class DeleteSkillView(DeleteView):
    model = ProgramSkill
    template_name = 'learning_tracker/delete_skill.html'
    context_object_name = 'program_skill'

    def get_success_url(self):
        return reverse('detail_program', kwargs={'pk': self.object.program.pk})

#Delete learning goal
class DeleteLearningGoalView(DeleteView):
    model = ProgramGoal
    template_name = 'learning_tracker/delete_learning_goal.html'
    context_object_name = 'program_goal'

    def get_success_url(self):
        return reverse('detail_program', kwargs={'pk': self.object.program.pk})


