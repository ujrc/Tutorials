app.service('cityService', function() {
    this.city = 'New York, NY'
});

app.service('weatherService', ["$resource", "$http", function($resource, $http) {
    this.GetWeather = function(city, days, apiKey) {

        var weatherAPI = $resource("http://api.openweathermap.org/data/2.5/forecast/daily", {
            callback: "JSON_CALLBACK"
        }, { get: { method: "JSONP" } });
        return weatherAPI.get({ q: city, cnt: days, appid: apiKey });
    };
   
}]);
// app.factory('apiFactory',["$http",function($http) { 
//     var obj = {content:null};
// $http.get('/static/webtweets/js/weather/config.json')
//             .success(function(data) {
//             obj.content = data;
//     });    

//     return obj;    
// }]);

app.factory('searchFactory', ["$resource", function($resource) {
    var link = "http://services.odata.org/OData/OData.svc/Products?$format=json";
    return $resource(link, {});
}]);
