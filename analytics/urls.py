from django.urls import path
from analytics.views import MonthlyTotalAnalyticsView, CategoryWiseAnalyticsView

urlpatterns = [
    path('monthly_total/',MonthlyTotalAnalyticsView.as_view(), name='monthly_total'),
    path('category_breakdown/',CategoryWiseAnalyticsView.as_view(), name='category_breakdown'),
]