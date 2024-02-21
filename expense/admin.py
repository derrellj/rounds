from django.contrib import admin
from .models import Expense


class ExpenseAdmin(admin.ModelAdmin):
    model = Expense
    list_display = [
        "date_time",
        "category",
        "income_spent",
        "amount",
        "memo",
        "total",
    ]


admin.site.register(Expense, ExpenseAdmin)
