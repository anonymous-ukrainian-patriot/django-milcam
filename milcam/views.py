# -*- coding: utf-8 -*-

# django-milcam
# milcam/views.py

from django.http import HttpResponse
from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

from milcam.models import Device
from milcam.forms import AddPhotoForm, AddPhotoAutonomousModeForm

__all__ = ['device', 'AddPhotoView', 'AddPhotoAutonomousModeView', ]


def device(request):
    """
    Create and return device id.
    """

    dev = Device.objects.create()

    return HttpResponse(dev.uuid)


class AddPhotoView(FormView):
    """
    Add photo view.
    """

    form_class = AddPhotoForm
    template_name = "milcam/add_photo.html"
    http_method_names = ('post', 'get', )

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):

        return super(AddPhotoView, self).dispatch(request, *args, **kwargs)

    @property
    def success_url(self):
        """
        Return self url.
        """

        return reverse('milcam_add_photo')

    def form_valid(self, form):
        """
        Save data.
        """

        form.save()

        return super(AddPhotoView, self).form_valid(form)


class AddPhotoAutonomousModeView(AddPhotoView):
    """
    Add photo after autonomous mode view.
    """

    form_class = AddPhotoAutonomousModeForm
