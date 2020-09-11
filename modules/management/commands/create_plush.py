from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.create_superuser(username="plush", password="plush")
        self.stdout.write(self.style.SUCCESS('Plush superuser created successfully'))
