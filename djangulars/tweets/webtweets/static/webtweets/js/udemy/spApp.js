myApp.controller('spaController',["$scope","$location","$log",function($scope,$location,$log) {
    
$log.info($location.path);
    }]);