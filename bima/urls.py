from django.urls import path
from .views import PolicyDetail, ClientList,ClientDetail
urlpatterns = [
    path('', ClientList.as_view()),
    path('<int:pk>/', PolicyDetail.as_view()),
    path('client/<int:pk>',ClientDetail.as_view()),
]