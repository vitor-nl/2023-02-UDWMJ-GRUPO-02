from django.urls import path
from .views import ClientSocialnetworkDetailView

app_name = 'clientsocialnetworks'
urlpatterns = [
    path('<int:pk>/', ClientSocialnetworkDetailView.as_view(), name='clientsocialnetwork-detail'),
    # Adicione outras URLs conforme necessário
]
