tutoApp.controller('tutoCtrl',function($scope,tutoFactory) {
    $scope.places=tutoFactory.getTuto();
    $scope.priceInfo={
        min:0,
        max:10000000
    }
$scope.newListing={};

$scope.addPlace=function(newListing) {
    newListing.image='default'
$scope.places.push(newListing);
$scope.newListing={};
}
$scope.editPlace=function(place){
    $scope.editListing=true;
    $scope.existingListing=place;
}
$scope.deletePlace=function(listing) {
    var index =$scope.places.indexOf(listing);
    $scope.places.splice(index,1);
    $scope.existingListing={};
    $scope.editListing=false;


    // body...
}
$scope.savePlaceEdit=function(){
    $scope.existingListing={};
    $scope.editListing=false;
}
$scope.sayHello=function() {
    console.log("Hello!");
}
});

// tutoApp.controller('tutoCtrl', function($scope, tutoFactory) {
//     $scope.places;
//     tutoFactory.getTuto().success(function(data) {
//         $scope.places = data;
//     }).error(function(error) {
//         console.log(error);
//     });
// });
