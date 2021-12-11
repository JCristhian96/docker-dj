from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, View
# Models
from .models import Person
# Forms 
from .forms import PersonForm

class Index(TemplateView):
    template_name = "core/index.html"


class PersonListView(ListView):
    model = Person
    template_name = "core/list-persons.html"
    context_object_name = "persons"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Lista de Personas"
        return context
    

class PersonCreateView(CreateView):
    model = Person
    template_name = "core/form-person.html"
    form_class = PersonForm
    success_url = reverse_lazy("core:list")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nueva Persona"
        return context
    

class PersonUpdateView(UpdateView):
    model = Person
    template_name = "core/form-person.html"
    form_class = PersonForm
    success_url = reverse_lazy("core:list")
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["title"] = "Editar Persona"
            return context
        
class PersonDeleteView(View):
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        Person.objects.get(id=pk).delete()
        return redirect(reverse_lazy("core:list"))