from django.db import models

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=30)
    days = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = "subscription"

