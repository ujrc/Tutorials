app.controller('bookController', function($scope) {
    $scope.clock = new Date();
    $scope.message="Hello!!";
    $scope.counter=0;
    $scope.add=function(amount) {$scope.counter+=amount;};
    $scope.substract=function(amount) {$scope.counter-=amount; };

});
