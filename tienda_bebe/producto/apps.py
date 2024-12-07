from django.apps import AppConfig

class ProductoConfig(AppConfig):
    name = 'producto'

    def ready(self):
        import producto.signals  # Asegúrate de que el archivo signals.py se registre
