# -*- coding: utf-8 -*-

# django-milcam
# milcam/models.py

from django.db import models
from django.utils.translation import ugettext_lazy as _

from uuidfield import UUIDField

__all__ = ['Device', ]


class Device(models.Model):
    """
    Device.
    """

    uuid = UUIDField(auto=True, verbose_name=_(u'device unique identifier'), unique=True, db_index=True)

    def __unicode__(self):

        return u"%s" % self.uuid

    class Meta:

        app_label = 'milcam'
        verbose_name = _(u'device')
        verbose_name_plural = _(u'devices')
