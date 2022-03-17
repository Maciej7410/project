from django import forms
from .models import Expense, Category


class ExpenseSearchForm(forms.ModelForm):

    start_date = forms.DateField()
    end_date = forms.DateField()


    choice_category = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=[(c.id, c.name) for c in Category.objects.all()])

    class Meta:
        model = Expense
        fields = ('name', 'start_date', 'end_date', 'choice_category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['start_date'].required = False
        self.fields['end_date'].required = False
        self.fields['choice_category'].required = False

