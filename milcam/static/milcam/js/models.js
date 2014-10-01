// django-milcam
// milcam/static/milcam/js/models.js

var DeviceModel = Backbone.RelationalModel.extend({
    url: function() {
        return sprintf('%(id)s?format=json', {id: this.id})
    }
});


var DevicesCollection = Backbone.Collection.extend({
    model: DeviceModel,
    url: sprintf('%(url)s?format=json', {url: Urls.api_dispatch_list(milcam.API_NAME, 'device')})
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
    url: sprintf('%(url)s?format=json', {url: Urls.api_dispatch_list(milcam.API_NAME, 'photo')})
});
