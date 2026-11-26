from django.apps import AppConfig


class AuthorsConfig(AppConfig):
    name = 'authors'

    
    def ready(self, *args, **kwargs):
        import authors.signals  # noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready