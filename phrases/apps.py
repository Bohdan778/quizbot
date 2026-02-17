from django.apps import AppConfig


class PhrasesConfig(AppConfig):
    name = "phrases"

    def ready(self):
        from bot.scheduler import start_scheduler
        start_scheduler()