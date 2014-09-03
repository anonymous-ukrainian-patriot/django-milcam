# -*- coding: utf-8 -*-

# django-milcam
# milcam/models.py

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from geoposition.fields import GeopositionField
from sorl.thumbnail import ImageField


__all__ = ['Photo', ]


class Photo(models.Model):
    """
    Photo with additional data model.
    """

    device = models.ForeignKey('milcam.Device', verbose_name=_(u'device'), db_index=True)
    image = ImageField(verbose_name=_(u'image'), upload_to=u'milcam/photo/')
    created = models.DateTimeField(verbose_name=_(u'datetime of creation'), db_index=True, default=datetime.now())
    position = GeopositionField()

    def __unicode__(self):

        return u'%s (%s)' % (self.device.uuid, self.created)

    class Meta:

        app_label = 'milcam'
        verbose_name = _(u'photo')
        verbose_name_plural = _(u'photo')
        ordering = ['-created', ]

    def save(self, *args, **kwargs):
        """
        Override because auto_now_add is ugly.
        """

        if not self.created:

            self.created = datetime.now()

        super(Photo, self).save(*args, **kwargs)
