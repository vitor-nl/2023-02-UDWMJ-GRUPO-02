from django.views.generic.detail import DetailView
from .models import ClientSocialnetwork

class ClientSocialnetworkDetailView(DetailView):
    model = ClientSocialnetwork
    template_name = 'clientsocialnetworks/clientsocialnetwork_detail.html'
    context_object_name = 'clientsocialnetwork'
