from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category, total_amount_spent, total_summary_per_year
from django.db.models import Q


class ExpenseListView(ListView):
    model = Expense
    date = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        # queryset = self.object_list

        form = ExpenseSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()

            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            category = form.cleaned_data.get('choice_category')

            if name or category:
                queryset = queryset.filter(Q(category_id__in=category, name__icontains=name)) #| Q(date__gt=start_date, date__lte=end_date))
            elif start_date and end_date:
                queryset = queryset.filter(date__gt=start_date, date__lt=end_date)



        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            total_amount_spent=total_amount_spent(Expense.objects.all()),
            total_summary_per_year=total_summary_per_year(Expense.objects.filter(date__year__isnull=False)),
            **kwargs)


class CategoryListView(ListView):
    model = Category
    paginate_by = 5
