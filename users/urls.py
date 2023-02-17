from django.urls import path
from .views import UsersListView, UserCreateView, UserDeleteView, UserDetailView, UserUpdateView

urlpatterns = [
    path('', UsersListView.as_view(), name='users_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/edit/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete', UserDeleteView.as_view(), name='user_delete'),
]
