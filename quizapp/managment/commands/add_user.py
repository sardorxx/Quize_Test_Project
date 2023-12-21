from pathlib import Path

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
User = get_user_model()

BASE_DIR = str(Path(__file__).resolve().parent.parent.parent.parent)+'/import_files/'


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(BASE_DIR+options['filename'][0]) as f:
            print(options)
            content = f.readlines()
            for user in content:
                User.objects.create(first_name=user[0], last_name=user[1], username=user[2], email=user[3],
                                    password=user[4])

        self.stdout.write(self.style.SUCCESS('Successfully'))
