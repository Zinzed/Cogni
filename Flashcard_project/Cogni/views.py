from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.shortcuts import render
from django.views.generic import(ListView, CreateView, UpdateView,DeleteView,)
from .models import Card
# Create your views here.
#ef main(request):
#   return render(request, 'Cogni/index.html')

class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")
    template_name = "Cogni/CardList.html"


#Below code from: https://realpython.com/django-flashcards-app/
class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    template_name = "Cogni/CardForm.html"
    success_url = reverse_lazy("CardCreate")
#TroubleShooting Code
    def form_valid(self, form):
        print("Form is valid")
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")
        return super().form_invalid(form)

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("CardList")

class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy('CardList')
    template_name = 'Cogni/Delete.html'