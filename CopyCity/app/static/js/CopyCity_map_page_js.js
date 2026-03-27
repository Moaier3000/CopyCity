async function initMap() {
    const [{ Map }, { AdvancedMarkerElement }] = await Promise.all([
        google.maps.importLibrary('maps'),
        google.maps.importLibrary('marker'),
    ]);

    const mapElement = document.querySelector('gmp-map');
    const innerMap = mapElement.innerMap;

    // Data from our Flask session
    const locations = window.recommendationsData;

    if (locations && locations.length > 0) {
        // Center the map on the first recommendation
        const firstPos = { 
            lat: parseFloat(locations[0].latitude), 
            lng: parseFloat(locations[0].longitude) 
        };
        innerMap.setCenter(firstPos);

        // Add markers for each city
        locations.forEach(loc => {
            new AdvancedMarkerElement({
                map: innerMap,
                position: { lat: parseFloat(loc.latitude), lng: parseFloat(loc.longitude) },
                title: loc.city,
            });
        });
        
        // Optional: Update the description text with the first city's info
        document.querySelector('.description h1').innerText = locations[0].city;
        document.querySelector('.description span').innerText = locations[0].description;
    }
}