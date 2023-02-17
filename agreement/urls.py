from django.urls import path
from .views import AgreementListView, AgreementCreateView, AgreementDetailView

urlpatterns = [
    path('', AgreementListView.as_view(), name='agrement_list'),
    path('<int:pk>/', AgreementDetailView.as_view(), name='agreement_detail'),
    path('create/<int:reserve_id>/', AgreementCreateView.as_view(), name='agreement_create'),
]
