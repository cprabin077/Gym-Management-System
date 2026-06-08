from django.db import models


class Status(models.TextChoices):
    INITIAL = "Initial"
    KHALTI_PROCESS = "Khalti Process"
    COMPLETED = "Completed"
    PENDING = "Pending"
    USER_CANCELLED = "User Cancelled"


# Create your models here.
class Transaction(models.Model):
    member = models.ForeignKey("member.Member", on_delete=models.RESTRICT)
    name = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.INITIAL
    )
    txn_id = models.CharField(max_length=50, null=True, blank=True)
    pidx = models.CharField(max_length=30, null=True, blank=True)
    location = models.TextField(null=True, blank=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = "transaction"

    def __str__(self):
        return f"{self.member} - {self.amount}"
