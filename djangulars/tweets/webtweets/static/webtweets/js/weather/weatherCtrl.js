app.controller('homeController', ["$scope", "$location","cityService",
    function($scope,$location, cityService) {
        $scope.city = cityService.city;
        $scope.$watch("city",function(){
        cityService.city=$scope.city;
        });
    
    $scope.submit=function() {
        $location.path("/forecast");
    };
    }]);

app.controller("forecastController", ["$scope","$resource","$routeParams","cityService","weatherService",
    function($scope,$resource,$routeParams,cityService,weatherService) {
        $scope.city = cityService.city;
        $scope.days=$routeParams.days || 2;
        $scope.apiKey="b1591813e0b2b090b07426643c217193";//default key
        // anotherKey='d9b8cbf7dfd2da7669dc3468a899a3b1'//weatherKey
        $scope.weatherAPIResult=weatherService.GetWeather($scope.city,$scope.days,$scope.apiKey);
        $scope.converttoFahrenheit=function(degKv) {
            return Math.round((1.8*(degKv-273))+32);
        }
        $scope.convertToDate=function(dt)
        {

        return  new Date(dt*1000);
        };
}]);


app.controller("searchController", ["$scope","searchFactory",function($scope,searchFactory) {
        
$scope.a="This is  Type head page";
$scope.search=function(searchParam){
searchFactory.get({

},function(data){
    $scope.data=data;
},function(error){
    console.error("The error occured while calling the search factory: ");
    console.error(error);
});
};
}]);