from django.core.management.base import BaseCommand
from django.db import IntegrityError
from your_app.models import YourUserModel  # Замените 'your_app' на реальное имя вашего приложения

class Command(BaseCommand):
    help = 'Your custom command'

    def handle(self, *args, **options):
        try:
            # Your code to create a new user instance and save it
            user = YourUserModel.objects.create(email='user@example.com', password='password')
            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user.email}'))
        except IntegrityError:
            # Handle the case where the email already exists
            self.stdout.write(self.style.WARNING("User with this email already exists."))
