from django.views.generic import ListView
from .models import Publication

class PublicationList(ListView):
    model = Publication
    template_name = 'publications-list.html'
    context_object_name = 'publications'
    ordering = ['-date']
    paginate_by = 5