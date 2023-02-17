from django.urls import path

from reservations.views import ReserveCreateView, ReserveListView, ReserveUpdateView, ReserveDetailView

urlpatterns = [
    path('create/', ReserveCreateView.as_view(), name='reserve_create'),
    path('list/', ReserveListView.as_view(), name='reserve_list'),
    path('<int:pk>/', ReserveDetailView.as_view(), name='reserve_detail'),
    path('<int:pk>/update/', ReserveUpdateView.as_view(), name='reserve_update'),
]
