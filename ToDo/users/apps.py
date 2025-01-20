from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Specifies default auto field for models
    name = 'users'  # The name of the app

    def ready(self):
        import users.signals  # Ensures signals are connected when the app is ready
