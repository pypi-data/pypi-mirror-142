from django.core.management import call_command
from django.core.management.base import BaseCommand

from marketmanager import __title__


class Command(BaseCommand):
    help = "Preloads data required for this app from ESI"

    def handle(self, *args, **options):
        call_command(
            "eveuniverse_load_types",
            __title__,
            "--category_id",
            "4", "7", "8", "18", "20", "32", "39", "40", "41", "42", "43", "65", "66", "87"
        )
