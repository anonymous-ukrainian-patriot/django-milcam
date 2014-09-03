// django-milcam
// milcam/static/milcam/js/models.js

var DeviceModel = Backbone.RelationalModel.extend({
    url: function() {
        return sprintf('%(id)s?format=json', {id: this.id})
    }
});


var DevicesCollection = Backbone.Collection.extend({
    model: DeviceModel,
    url: '/milcam/api/v1/device/?format=json'  // fckng hardcoded api version
});


var PhotoModel = Backbone.RelationalModel.extend({
    url: function() {
        return sprintf('%(id)s?format=json', {id: this.id})
    },
    relations: [
        {
            type: Backbone.HasOne,
            key: 'device',
            relatedModel: 'DeviceModel',
            collectionType: 'DevicesCollection',
            autoFetch: true,
            reverseRelation: {
                key: 'device_photos',
                includeInJSON: 'id'
            }
        }
    ]
});


var PhotosCollection = Backbone.Collection.extend({
    model: PhotoModel,
    url: '/milcam/api/v1/photo/?format=json'  // fckng hardcoded api version
});
