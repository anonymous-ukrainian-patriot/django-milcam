# -*- coding: utf-8 -*-

# django-milcam
# milcam/settings.py

from django.conf import settings

__all__ = ['CURRENT_API_NAME', ]

CURRENT_API_NAME = getattr(settings, 'MILCAM_CURRENT_API_NAME', u'v1')
