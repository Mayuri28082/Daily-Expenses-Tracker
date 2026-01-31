from rest_framework import serializers
from expenses.models import Expense
from decimal import Decimal, InvalidOperation


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'category', 'date', 'note']

    def validate_amount(self, value):
        try:
            value = Decimal(value)
        except (InvalidOperation, TypeError):
            raise serializers.ValidationError("Amount must be a valid decimal number.")

        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")

        return value