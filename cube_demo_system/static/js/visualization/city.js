var map;
var info;

function style(feature) {
    return {
        color: feature.properties.stroke,
        weight: feature.properties.strokeWidth,
        opacity: feature.properties.strokeOpacity,
        dashArray: '3',
        fillColor: feature.properties.fill,
        fillOpacity: feature.properties.fillOpacity
    };
}

function onEachFeature(feature, layer) {
	layer.on({
		mouseover: highlightFeature,
		mouseout: resetHighlight,
		click: showModal,
	});
}

$(document).ready(function(){
	map = L.map('id-city-map').setView([39.687672, -121.644780], 9);

	L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
			attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
			maxZoom: 18,
			id: 'mapbox.streets',
			accessToken: 'pk.eyJ1IjoicmlnaHRwZXRlciIsImEiOiJjanF2cDZkbXgweG55M3huM3Q4M2pzNmQyIn0.CRt9olNUZxwwdFFpS-n3wQ'
	}).addTo(map);
})

function highlightFeature(e) {
  var layer = e.target;

  layer.setStyle({
      weight: 5,
      color: '#666',
      dashArray: '',
      fillOpacity: 0.8
  });

  if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
      layer.bringToFront();
  }

	info.update(layer.feature.properties);
}

function resetHighlight(e) {
	cityGeoJson.resetStyle(e.target);
	info.update();
}

function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
}

function showModal(e) {
	var layer = e.target;

	console.log(e.target.id);
	$('#modal_title').html("City id: " + layer.feature.properties.cityName)
	$('#city_modal').modal('show');
}

