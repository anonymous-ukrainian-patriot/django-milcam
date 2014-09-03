// django-milcam
// milcam/static/milcam/js/views.js

var PhotosMapView = Backbone.View.extend({

    tagName: 'div',
    el: '#id-photos-view',
    events: {
        "click tr.photo": "photoTablePhotoClick"
    },
    photoInfoWindowTpl: _.template($('#id-photo-infoWindow-tpl').html()),
    photosTableTpl: _.template($('#id-photos-table-tpl').html()),

    photos: new PhotosCollection(),
    markers: [],
    infoWindows: [],
    markerBounds: new google.maps.LatLngBounds(),
    mapOptions: {
        center: new google.maps.LatLng(0, 0),
        zoom: 6,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    },
    map: new google.maps.Map(document.getElementById("id-photos-map"), this.mapOptions),

    initialize: function() {
        var self = this;
        this.initDOMElements();
        self.photos.fetch({  // setting fetch callback for right data rendering
            success: function(model, response){
              self.render();
            }
        });
        self.photos.fetch();  // fetching last day photos
    },

    initDOMElements: function() {
        this.$photosTable = $('#id-photos-table');
    },

    render: function() {
        var self = this;
        _.each(self.photos.models, function(photo) {
            self.showPhotoOnMap(photo);
        });
        self.map.fitBounds(self.markerBounds);
        self.renderPhotosTable();
    },

    renderPhotosTable: function() {
        this.$photosTable.html(this.photosTableTpl({photos: this.photos.models}));
        this.initTableSorter();
    },

    initTableSorter: function() {
        $('.tablesorter').tablesorter({
            cancelSelection: false,
            cssAsc: 'dsc',
            cssDesc: 'asc',
            cssHeader: 'header',
            headers: {
                0: {
                    sorter: false
                },
                1: {
                    sorter: false
                }
            }
        });
    },

    showPhotoOnMap: function(photo) {
        var self = this;
        var Latlng = new google.maps.LatLng(photo.get('latitude'), photo.get('longitude')),
                marker = new google.maps.Marker({
                    position: Latlng,
                    map: self.map,
                    title: photo.get('created').toLocaleString()
                }),
                infowindow = new google.maps.InfoWindow({
                    content: self.photoInfoWindowTpl({photo: photo})
                });

        google.maps.event.addListener(marker, 'click', function() {
            self.closeAllInfoWindows();
            infowindow.open(self.map ,marker);
        });
        self.markerBounds.extend(Latlng);
        self.markers[photo.get('id')] = marker;
        self.infoWindows[photo.get('id')] = infowindow;
    },

    closeAllInfoWindows: function() {
        _.each(this.infoWindows, function(infowindow) {
            infowindow.close();
        });
    },

    photoTablePhotoClick: function(el) {
        var $el = $(el.currentTarget);
        $el.siblings().removeClass('active');
        $el.addClass('active');
        new google.maps.event.trigger(this.markers[$el.data('photo-id')], 'click');
    }

});
