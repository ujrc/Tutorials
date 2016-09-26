myApp.controller('secondCtrl', ["$scope", "$http", function(
    $scope, $http) {

    $scope.name = "Jeanne";

    $http.get("/api/tweets/").success(function(result) {
            $scope.tweets = result;
        })
        .error(function(data, status) {
            console.log(data);
        });

    $scope.newTweet = '';
    $scope.user = 1;
    $scope.addTweet = function() {
    $http.post("/api/tweets/", { user: $scope.user, newTweet: $scope.newTweet })
        .success(function(result){
            $scope.newTweet=result;
            $scope.user=result;
            $scope.newTweet='';
        }).error(function(data,status){
            console.log(data);
        });
    };
}]);
