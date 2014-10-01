# -*- coding: utf-8 -*-

# django-milcam
# milcam/urls.py

from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from tastypie.api import Api

from milcam.views import device, AddPhotoView, AddPhotoAutonomousModeView
from milcam.forms import AddPhotoForm, AddPhotoAutonomousModeForm
from milcam.api import DeviceResource, PhotoResource
from milcam.settings import CURRENT_API_NAME

# making api
api = Api(api_name=CURRENT_API_NAME)
api.register(DeviceResource())
api.register(PhotoResource())


urlpatterns = patterns('',
    # third part urls
    url(r'^jsreverse/$', 'django_js_reverse.views.urls_js', name='js_reverse'),
    # milcam urls
    url(r'^device/$', device, name='milcam_device'),  # get device id
    url('^photo/$', AddPhotoView.as_view(form_class=AddPhotoForm), name='milcam_add_photo', ),  # add photo
    url('^photo/autonomous/$', AddPhotoAutonomousModeView.as_view(form_class=AddPhotoAutonomousModeForm), name='milcam_add_photo_autonomous_mode', ),  # add photo after autonomous mode
    url('^map/$', login_required(TemplateView.as_view(template_name="milcam/map.html")), name='map', ),  # last day photos map
    url(r'^api/', include(api.urls), name='milcam_api'),  # api
)
