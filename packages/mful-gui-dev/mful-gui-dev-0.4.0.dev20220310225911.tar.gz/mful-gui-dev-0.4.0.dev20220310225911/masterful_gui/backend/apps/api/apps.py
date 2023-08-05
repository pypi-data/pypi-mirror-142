from typing import Optional, Any

from django.apps import AppConfig


class ApiConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'masterful_gui.backend.apps.api'