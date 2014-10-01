# -*- coding: utf-8 -*-

# django-milcam
# milcam/api.py

from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authorization import ReadOnlyAuthorization

from milcam.models import Device, Photo

__all__ = ['DeviceResource', 'PhotoResource', ]


class DeviceResource(ModelResource):
    """
    Device resource.
    """

    class Meta:

        queryset = Device.objects.all()
        resource_name = 'device'
        allowed_methods = ['get', ]
        filtering = {
            'name': ALL,
        }
        authorization = ReadOnlyAuthorization()


class PhotoResource(ModelResource):
    """
    Photo resource.
    """

    device = fields.ForeignKey('milcam.api.DeviceResource', 'device', full=True)

    class Meta:

        queryset = Photo.objects.all()
        resource_name = 'photo'
        allowed_methods = ['get', ]
        filtering = {
            'device': ALL_WITH_RELATIONS,
            'created': ALL,
        }
        authorization = ReadOnlyAuthorization()

    def dehydrate(self, bundle):

        bundle.data['latitude'] = bundle.obj.position.latitude
        bundle.data['longitude'] = bundle.obj.position.longitude

        return bundle
