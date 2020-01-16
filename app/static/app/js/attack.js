function locateLaunchPads(){
    var lpJSON = {"launchpads":[{"name":"lp1","lat":"10.358151","lng":"76.68457"},{"name":"lp2","lat":"28.690588","lng":"77.124023"},{"name":"lp3","lat":"18.812718","lng":"73.520508"},{"name":"lp4","lat":"25.244696","lng":"84.023438"},]  }
    
    var launchpad;
    
    for(lp in lpJSON.launchpads){
        lat=parseFloat(lpJSON.launchpads[lp].lat); 
        lng=parseFloat(lpJSON.launchpads[lp].lng); 
        L.marker([lat, lng]).addTo(map);
    }
}