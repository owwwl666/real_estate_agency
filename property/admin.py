from django.contrib import admin

from .models import Flat
from .models import UserComplaint
from .models import Owner


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
        "owners_phonenumber",
        "owner_pure_phone",
    ]
    list_editable = ["new_building"]
    list_filter = [
        "new_building",
        "floor",
        "rooms_number",
        "living_area",
    ]
    raw_id_fields = ["likes"]


class UserComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["user", "flat"]


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ["owner"]
    raw_id_fields = ["possessions"]


admin.site.register(Flat, FlatAdmin)
admin.site.register(UserComplaint, UserComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
