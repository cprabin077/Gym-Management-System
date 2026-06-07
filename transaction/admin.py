from django.contrib import admin

from transaction.models import Transaction

# Register your models here
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "member",
        "amount",
        "status",
        "txn_id",
        "pidx",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "member__name",
        "txn_id",
        "pidx",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)
