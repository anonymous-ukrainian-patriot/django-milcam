# -*- coding: utf-8 -*-

# django-milcam
# milcam/admin.py

from django.contrib import admin
from django.utils.html import format_html

from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.admin import AdminImageMixin

from milcam.models import Device, Photo

__all__ = ['PhotoAdmin', 'DeviceAdmin', ]


class DeviceAdmin(AdminImageMixin, admin.ModelAdmin):
    """
    Customize Device model for admin area.
    """

    list_display = ['uuid', ]
    search_fields = ['uuid', ]


class PhotoAdmin(AdminImageMixin, admin.ModelAdmin):
    """
    Customize Photo model for admin area.
    """

    list_display = ['device', 'created', 'position', 'thumb', ]
    search_fields = ['device__uuid', ]
    list_filter = ['device', ]
    date_hierarchy = 'created'

    def thumb(self, obj):

        if obj.image:
            thumb = get_thumbnail(obj.image.file, u"60x60")

            return format_html(u'<a href="{0}"><img src="{1}" width="{2}px" height="{3}px" /></a>', obj.image.url, thumb.url, thumb.width, thumb.height)


# register admin customize classes
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Device, DeviceAdmin)
