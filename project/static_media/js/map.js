

var geocoder;
var map, layer;
function initialize() {
  geocoder = new google.maps.Geocoder();
  var latlng = new google.maps.LatLng(35.399756, -79.766613);
  var mapOptions = {
    zoom: 7,
    center: latlng
  }

  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);


  var layer = new google.maps.KmlLayer({
    url: 'http://colleenmcenaney.com/kml/gun.kml'
  });

  layer.setMap(map);
}

function codeAddress() {
  var address = document.getElementById('address').value;
  geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == google.maps.GeocoderStatus.OK) {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location
      });
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}

google.maps.event.addDomListener(window, 'load', initialize);

$('#box').keyup(function(){
   var valThis = $(this).val().toLowerCase();
    $('.navList>li').each(function(){
     var text = $(this).text().toLowerCase();
        (text.indexOf(valThis) == 0) ? $(this).show() : $(this).hide();            
   });
});

