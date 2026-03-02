from django.urls import path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.BirthdayCreateView.as_view(), name='create'),
    path('list/', views.BirthdayListView.as_view(), name='list'),
    path('<pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    path('<pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    path('<pk>/delete/', views.BirthdayDeleteView.as_view(), name='delete'),
    path('<pk>/comment/', views.add_comment, name='add_comment'),
]
