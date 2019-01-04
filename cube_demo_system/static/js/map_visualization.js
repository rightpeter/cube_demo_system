FILL_COLORS=["0", "58", "118", "238"]
data = []
dateRange = 0
minDate = ""


function getFilledColor(fillColor, percentage){
  return "hsl("+fillColor+", "+Math.min(100, (percentage*100).toFixed(2))+"%, 60%)"
}

function showModal(e) {
	console.log(e.target.id);
	$('#modal_title').html("County id: " + e.target.id)
	$('#county_modal').modal('show');
}

function updateMap(val, svg, range, data){
  var topicIndex = parseInt(document.querySelector('input[name="topic_filter"]:checked').value);
  var fillColor = FILL_COLORS[topicIndex];
  var dict = new Set();
  var cellWeight = new Map();
  // var min = 100;
  // var max = 0;
  var index;
  for(index in data){
      let i = data[index];
      if( i.time < val+range && i.time >= val && i.location.length && (topicIndex == 3 || i.topics[topicIndex] > 0.3 ) ){
        var locationIndex;
        for(locationIndex in i.location){
          let location = i.location[locationIndex]
          dict.add(location);

          if( !cellWeight.has(location)) {
            cellWeight.set(location, 0)
          }

          if (topicIndex == 3 )
              svg.getElementById(location).setAttribute("fill", "hsl(238, 100%, 80%)");
          else {
            //svg.getElementById(location).setAttribute("fill", getFilledColor(fillColor, {{ i.topics }}[topicIndex]));
            cellWeight.set(location, cellWeight.get(location) + i.topics[topicIndex])
            // if(cellWeight.get("{{ location }}") > max) max = cellWeight.get(location)
            // if (cellWeight.get("{{ location }}") < min ) min = cellWeight.get("{{ location }}")
          }
        }

      } else{
        // change the color back to default color
        for(index in i.location){
          let location = i.location[index]
          if (!dict.has(location) && location != "None"){
            svg.getElementById(location).setAttribute("fill", "#CCCCCC");
          }
        }

      }
  }
  // var range = max - min;
  if(topicIndex!=3){
      cellWeight.forEach(function(value, location, map){
        svg.getElementById(location).setAttribute("fill", getFilledColor(fillColor, value));
      })
    }
}


function updateDate(originDate, id, val){
  var minDate = new Date(originDate.toDateString())
  minDate.setDate(minDate.getDate() + val);
  var minDateString = minDate.toDateString()
  minDate.setDate(minDate.getDate() + 2);
  document.getElementById(id).innerHTML= minDateString + " - " + minDate.toDateString();
}

function updateTimeInput(range, data, dateRange, minDate) {
    var val = document.getElementById("timeline_slider").value;
    var svg = document.getElementById("map_current").contentDocument;
    var svg_prev = document.getElementById("map_prev").contentDocument;
    var svg_next = document.getElementById("map_next").contentDocument;
    if (range == 3)
      document.getElementById("show_all_checkbox").checked=false;
    var dict = new Set();
    var minDate = new Date(minDate);
    val = parseInt(val)
    updateDate(minDate, "selectedDate_current", val);
    updateMap(val, svg, range, data);
    if(val>0){
      updateMap(val-range, svg_prev, range, data);
      updateDate(minDate, "selectedDate_prev", val-range);
    }
    else{
      updateMap(-1, svg_prev,0, data);
      document.getElementById("selectedDate_prev").innerHTML = "";
    }

    if (val < dateRange && range != dateRange){
      updateMap(val+range, svg_next, range, data);
      updateDate(minDate, "selectedDate_next", val+range);
    }
    else{
      updateMap(-1, svg_next,0, data);
      document.getElementById("selectedDate_next").innerHTML = "";
    }
}


function switchShowAll(data, dateRange, minDate){
  var chk=document.getElementById("show_all_checkbox").checked;
  if (chk){
    document.getElementById("timeline_slider").value = "0";
    updateTimeInput(dateRange, data, dateRange, minDate);
  }
  else {
    updateTimeInput(3, data, dateRange, minDate);
  }
}
