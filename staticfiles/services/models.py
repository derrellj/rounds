from django.db import models


class Service(models.Model):
    PEDICURE = "Pedicure"
    MANICURE = "Manicure"
    MAKEUP = "Make Up"
    OTHER = "Other"

    SERVICE_CHOICES = [
        (PEDICURE, "Pedicure"),
        (MANICURE, "Manicure"),
        (MAKEUP, "Make Up"),
        (OTHER, "Other"),
    ]

    name = models.CharField(max_length=100)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
