from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from datetime import date

from .serializers import TransactionSerializer
from .models import Transaction

class TransactionList (generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            validated_data = serializer.validated_data

            transaction_instance = serializer.create(validated_data)

            book = validated_data['book']

            if book.stock < 1:
                return Response({'error': 'No hay stock disponible'}, status=status.HTTP_400_BAD_REQUEST)

            book.stock -= 1
            book.save()

            transaction_instance.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TransactionDetail (generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def update(self, *args, **kwargs):
        instance = self.get_object()
        oldLoanStatus = instance.loanStatus

        with transaction.atomic():
            if (oldLoanStatus == 'inCourse'):
                instance.loanStatus = 'returned'
                instance.returnDate = date.today()
                instance.save()

            if oldLoanStatus != instance.loanStatus and instance.loanStatus == 'returned':
                instance.book.stock += 1
                instance.book.save()
            else:
                return Response({'error': 'El producto no se encuentra con un préstamo activo'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
