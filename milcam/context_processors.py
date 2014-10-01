# -*- coding: utf-8 -*-

# django-milcam
# milcam/context_processors.py

from milcam.settings import CURRENT_API_NAME

__all__ = ['api_name', ]


def api_name(request):
    """
    Return current api name.
    """

    return {'API_NAME': CURRENT_API_NAME, }
