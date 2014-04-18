<script type="text/javascript"
src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDSXRVKo3e9gwZ8L2zmA5EJ5VGD2y654dU&amp;sensor=false">
</script>
<script type="text/javascript">
  function initialize() {
    var myLatlng = new google.maps.LatLng({{team.latitude}},{{team.longitude}});
    var mapOptions = {
      center: myLatlng,
      zoom: 8
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),
      mapOptions);
    var marker = new google.maps.Marker({
      position: myLatlng,
      map: map
    });
  }
  google.maps.event.addDomListener(window, 'load', initialize);
</script>

