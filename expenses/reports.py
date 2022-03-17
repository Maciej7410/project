from collections import OrderedDict

from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from .models import Expense


def summary_per_category(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))


def total_amount_spent(queryset):
    return queryset.aggregate(Sum('amount'))


def total_summary_per_year(queryset):
    return queryset.values('date__year').annotate(sum_year=Sum('amount'))

