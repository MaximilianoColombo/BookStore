from django.urls import path,include
from .views import TransactionList, TransactionDetail

urlpatterns = [
    path('transactions/', TransactionList.as_view()),
    path('transactions/<int:pk>/', TransactionDetail.as_view()),
]