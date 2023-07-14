from django.db import migrations
import phonenumbers


def normalizes_phone_number(apps, schema_editor):
    Flat = apps.get_model("property", "Flat")
    flats = Flat.objects.all()
    for flat in flats:
        phone_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(phone_number):
            flat.owner_pure_phone = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0005_auto_20230713_2226'),
    ]

    operations = [
        migrations.RunPython(normalizes_phone_number),
    ]
