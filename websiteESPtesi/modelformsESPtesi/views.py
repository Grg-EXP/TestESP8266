from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from modelformsESPtesi.models import ESPdata

# view for the index page
class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'data_list'
    template_name = 'modelformsESPtesi/index.html'

    def get_queryset(self):
        return ESPdata.objects.all()

# view for the product entry page
class ESPdataEntry(CreateView):
    model = ESPdata
    # the fields mentioned below become the entry rows in the generated form
    fields = ['temperatura', 'umidita', 'pressione','pioggia', 'posizione']

# view for the product update page
class ESPdataUpdate(UpdateView):
    model = ESPdata
    # the fields mentioned below become the entyr rows in the update form
    fields = ['temperatura', 'umidita', 'pressione', 'pioggia', 'posizione']

# view for deleting a product entry
class ESPdataDelete(DeleteView):
    model = ESPdata
    # the delete button forwards to the url mentioned below.
    success_url = reverse_lazy('modelformsESPtesi:index')