from django.urls import path
from expenses.views import AddExpenseView, UpdateExpenseView, DeleteExpenseView, ListExpenseView

urlpatterns = [
    path('add/',AddExpenseView.as_view(), name='add_expense'),
    path('update/<int:id>/',UpdateExpenseView.as_view(), name='update_expense'),
    path('delete/<int:id>/',DeleteExpenseView.as_view(), name='delete_expense'),
    path('list/',ListExpenseView.as_view(), name='list_expenses'),
]