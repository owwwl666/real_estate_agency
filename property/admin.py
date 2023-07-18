from django.contrib import admin

from .models import Flat
from .models import UserComplaint
from .models import Owner


class OwnersInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ["owner"]


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    inlines = [
        OwnersInline,
    ]
    search_fields = [
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
    raw_id_fields = ["who_likes"]


@admin.register(UserComplaint)
class UserComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["user", "flat"]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ["owner"]
    raw_id_fields = ["possessions"]
