app.service('cityService', function() {
    this.city = 'New York, NY'
});
app.service('weatherService', ['$resource', function($resource) {
    this.GetWeather=function(city, days,apiKey) {
       var weatherAPI=$resource("http://api.openweathermap.org/data/2.5/forecast/daily",{
            callback:"JSON_CALLBACK"},{get:{method:"JSONP"}});

        return weatherAPI.get({q:city,cnt:days,appid:apiKey});
    };
}]);

app.factory('searchFactory',["$resource", function($resource){
var link="http://services.odata.org/OData/OData.svc/Products?$format=json";
return $resource(link,{});
}]);