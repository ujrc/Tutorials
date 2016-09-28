app.controller('homeController', ["$scope", "$location", "cityService",
    function($scope, $location, cityService) {
        $scope.city = cityService.city;
        $scope.$watch("city", function() {
            cityService.city = $scope.city;
        });
        $scope.submit = function() {
            $location.path("/forecast");
        }
    }
]);

app.controller("forecastController", ["$scope", "$routeParams", "$http", "cityService", "weatherService",
    function($scope, $routeParams, $http, cityService, weatherService) {
        $scope.city = cityService.city;
        $scope.days = $routeParams.days || 2;

        $scope.apiKey = $http.get('/static/webtweets/js/weather/config.json')
            .then(function(response) {
                return response.data;
            });
    console.log($scope.apiKey);
       $scope.weatherAPIResult = weatherService.GetWeather($scope.city, $scope.days, $scope.apiKey);
        $scope.converttoFahrenheit = function(degKv) {
            return Math.round((1.8 * (degKv - 273)) + 32);
        }
        $scope.convertToDate = function(dt) {
            return new Date(dt * 1000);
        };
    }
]);


app.controller("searchController", ["$scope", "searchFactory", function($scope, searchFactory) {

    $scope.a = "This is  Type head page";
    $scope.search = function(searchParam) {
        searchFactory.get({

        }, function(data) {
            $scope.data = data;
        }, function(error) {
            console.error("The error occured while calling the search factory: ");
            console.error(error);
        });
    };
}]);
