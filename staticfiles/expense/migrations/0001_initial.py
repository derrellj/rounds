# Generated by Django 5.0.2 on 2024-02-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('customer_number', models.CharField(blank=True, max_length=15, null=True)),
                ('category', models.CharField(choices=[('pedicure', 'Pedicure'), ('manicure', 'Manicure'), ('makeup', 'Makeup'), ('other', 'Other')], max_length=20)),
                ('income_spent', models.CharField(choices=[('Income', 'Income Received'), ('Expenses', 'Money Spent'), ('Loss', 'Money Lost')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('memo', models.TextField(blank=True, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=10)),
            ],
        ),
    ]