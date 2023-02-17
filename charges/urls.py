from django.urls import path
from .views import ProfitListView, IncomeListView, IncomeCreateView, IncomeDeleteVieW, IncomeUpdateView, \
    OutcomeListView, OutcomeCreateView, charges_default, export_users_xls

urlpatterns = [
    path('income/', IncomeListView.as_view(), name='income'),
    path('income/create/', IncomeCreateView.as_view(), name='income_create'),
    path('income/<int:pk>/update/', IncomeUpdateView.as_view(), name='income_update'),
    path('income/<int:pk>/delete/', IncomeDeleteVieW.as_view(), name='income_delete'),
    path('outcome/', OutcomeListView.as_view(), name='outcome'),
    path('profit/', ProfitListView.as_view(), name='profit'),
    path('outcome/create/', OutcomeCreateView.as_view(), name='outcome_create'),
    path('charges_dflt', charges_default, name='default'),
    path('xls/', export_users_xls, name='export_xls'),
]
