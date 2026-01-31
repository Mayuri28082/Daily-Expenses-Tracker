import logging
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions, status
from expenses.models import Expense
from expenses.serializers import ExpenseSerializer
from rest_framework.response import Response
from datetime import datetime



logger = logging.getLogger(__name__)


class AddExpenseView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            serializer = ExpenseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Expense creation error: {str(e)}")
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateExpenseView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, id):
        try:
            expense = get_object_or_404(Expense, id=id, user=request.user)
            if not expense:
                return Response({"error": "You do not have permission to access this expense."}, status=status.HTTP_403_FORBIDDEN)

            serializer = ExpenseSerializer(expense, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(f"Expense update error: {str(e)}")
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class DeleteExpenseView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, id):
        try:
            expense = get_object_or_404(Expense, id=id, user=request.user)
            if not expense:
                return Response({"error": "You do not have permission to access this expense."}, status=status.HTTP_403_FORBIDDEN)

            expense.delete()
            return Response({"message": "Expense deleted successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Expense deletion error: {str(e)}")
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ListExpenseView(APIView):
    """
    Date format must be YYYY-MM-DD.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            expenses = Expense.objects.filter(user=request.user)

            start_date = request.query_params.get('start_date')
            end_date = request.query_params.get('end_date')
            category = request.query_params.get('category')

            # Validate date formats
            try:
                if start_date:
                    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                if end_date:
                    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError:
                return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

            # Validate date range
            if start_date and end_date and start_date > end_date:
                return Response({"error": "start_date cannot be greater than end_date"}, status=status.HTTP_400_BAD_REQUEST)

            if start_date:
                expenses = expenses.filter(date__gte=start_date)
            if end_date:
                expenses = expenses.filter(date__lte=end_date)
            if category:
                expenses = expenses.filter(category=category)

            serializer = ExpenseSerializer(expenses, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Expense listing error: {str(e)}")
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
