import logging
from rest_framework import permissions
from rest_framework.views import APIView
from expenses.models import Expense
from rest_framework.response import Response
from datetime import date


logger = logging.getLogger(__name__)


class MonthlyTotalAnalyticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            today = date.today()
            month_start = today.replace(day=1)

            expenses = Expense.objects.filter(user=request.user, date__gte=month_start, date__lte=today)

            total_amount = sum(exp.amount for exp in expenses)
            transactions = expenses.count()

            return Response({
                "month": today.strftime("%Y-%m"),
                "total_amount": total_amount,
                "transactions": transactions
            })
        except Exception as e:
            logger.error(f"Monthly analytics error: {str(e)}")
            return Response({"error": "An unexpected error occurred"}, status=500)


class CategoryWiseAnalyticsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            expenses = Expense.objects.filter(user=request.user)
            category_totals = {}

            for expense in expenses:
                category_totals[expense.category] = (category_totals.get(expense.category, 0) + expense.amount)

            return Response(category_totals)
        except Exception as e:
            logger.error(f"Category analytics error: {str(e)}")
            return Response({"error": "An unexpected error occurred"}, status=500)









