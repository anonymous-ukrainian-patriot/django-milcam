# -*- coding: utf-8 -*-

# django-milcam
# milcam/forms.py

from django import forms
from django.utils.translation import ugettext_lazy as _

from annoying.decorators import autostrip

from milcam.models import Photo, Device

__all__ = ['AddPhotoForm', 'AddPhotoAutonomousModeForm', ]


@autostrip
class AddPhotoForm(forms.ModelForm):
    """
    Add photo form.
    """

    device = forms.ModelChoiceField(label=_(u'device'), queryset=Device.objects.all(), empty_label=None, to_field_name='uuid')

    class Meta:

        model = Photo
        fields = ['device', 'image', 'position', ]


@autostrip
class AddPhotoAutonomousModeForm(AddPhotoForm):
    """
    Add photo after autonomous mode form.
    """

    created = forms.DateTimeField(label=_(u'created'), input_formats=('%m/%d/%Y %H:%M:%S', ))

    class Meta:

        model = Photo
        fields = ['device', 'image', 'position', 'created', ]
