from django.contrib.auth.models import User
user = User.objects.create_superuser(username="plush", password="plush")
