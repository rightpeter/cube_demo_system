var map;
var info;
var TOPICS=['Death & Injury', 'Reconstruction', 'Property Loss']

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

function showModal(e) {
	var layer = e.target;
	var city = layer.feature.properties.cityName

  var cellId = [topic, city, time].join('_')
	$('#modal_title').html("City: " + city + ",  Topic: " + TOPICS[parseInt(topic)] +", Date: "+time);
  $('#summary-content').html('<div class="row form-group"> <ul class="form-group" id="key-phrases-list"></ul></div>');
  var keyPhrase;
  if (keyPhrases[cellId]){
    var keys = Object.keys(keyPhrases[cellId])
    for (keyPhrase in keys){
      var $keyPhrase = $('<li class="key-phrase-li"> <span class="label label-primary">'+ keys[keyPhrase]+' </span></li>')
      $('#key-phrases-list').append($keyPhrase)
      var $keySentence = $('<div class="row form-group"><p>' + keyPhrases[cellId][keys[keyPhrase]]+ '</p></div>')
      $('#summary-content').append($keySentence)
    }
  }
  if (images[topic][city])
    $('#fire_image').attr('src', "/static/" + images[topic][city][time]);
	$('#city_modal').modal('show');
}
