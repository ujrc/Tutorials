app.controller('homeController', ["$scope", "$location","cityService",
    function($scope,$location, cityService) {
        $scope.city = cityService.city;
        $scope.$watch("city",function(){
        cityService.city=$scope.city;
        });
    
    $scope.submit=function() {
        $location.path("/forecast");
    }
    }]);

app.controller("forecastController", ["$scope","$resource","$routeParams","cityService",
    function($scope,$resource,$routeParams,cityService) {
        $scope.city = cityService.city;
        $scope.days=$routeParams.days || 2;
        $scope.weatherAPI=$resource("http://api.openweathermap.org/data/2.5/forecast/daily",{
            callback:"JSON_CALLBACK"},{get:{method:"JSONP"}});
        
        $scope.apiKey="b1591813e0b2b090b07426643c217193";//default key
        // anotherKey='d9b8cbf7dfd2da7669dc3468a899a3b1'//weatherKey
        $scope.weatherAPIResult=$scope.weatherAPI.get({q:$scope.city,cnt:$scope.days,appid:$scope.apiKey});
        $scope.converttoFahrenheit=function(degKv) {
            return Math.round((1.8*(degKv-273))+32);
        }
        $scope.convertToDate=function(dt)
        {

        return  new Date(dt*1000);
        };
    }]);

