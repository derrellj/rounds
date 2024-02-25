from django.db import models


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("pedicure", "Pedicure"),
        ("manicure", "Manicure"),
        ("makeup", "Makeup"),
        ("other", "Other"),
    ]

    INCOME_SPENT_CHOICES = [
        ("Income", "Income Received"),
        ("Expenses", "Money Spent"),
        ("Loss", "Money Lost"),
    ]

    date_time = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.EmailField(blank=True, null=True)
    customer_number = models.CharField(max_length=15, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    income_spent = models.CharField(max_length=10, choices=INCOME_SPENT_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    memo = models.TextField(blank=True, null=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, editable=False
    )

    def save(self, *args, **kwargs):
        if self.income_spent == "Income":
            self.total += self.amount
        elif self.income_spent == "Expenses":
            self.total -= self.amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date_time} - {self.customer_name} - {self.memo[:50]} - {self.category} - {self.income_spent} - {self.total}"
