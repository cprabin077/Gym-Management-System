from django.contrib import admin
from transaction.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "member",
        "name",
        "amount",
        "status",
        "txn_id",
        "pidx",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "name",
        "txn_id",
        "pidx",
        "member__name",  # adjust if Member uses a different field
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)

    fieldsets = (
        (
            "Transaction Information",
            {
                "fields": (
                    "member",
                    "name",
                    "amount",
                    "status",
                )
            },
        ),
        (
            "Payment Details",
            {
                "fields": (
                    "txn_id",
                    "pidx",
                    "location",
                )
            },
        ),
        (
            "Timestamps",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )