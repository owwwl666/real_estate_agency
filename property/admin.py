from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = [
        "owner",
        "town",
        "address",
    ]
    readonly_fields = ["created_at"]
    list_display = [
        "address",
        "price",
        "new_building",
        "construction_year",
        "town",
    ]
    list_editable = ["new_building"]
    list_filter = [
        "new_building",
        "floor",
        "rooms_number",
        "living_area",
    ]


admin.site.register(Flat, FlatAdmin)
