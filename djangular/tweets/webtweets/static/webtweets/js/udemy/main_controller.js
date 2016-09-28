myApp.controller('MainCtrl',["$scope","$log","$resource","$timeout","$filter",function(
    $scope,$log,$resource,$timeout,$filter) {
    $scope.name="Jeanne"
    $timeout(function(){
        $scope.name='Hello All!'
    },3000);
    $scope.handle='';
    $scope.lowerCasehandle=function(){
        return $filter('lowercase')($scope.handle);
    };
    $scope.$watch("handle", function(newValue,oldValue){
        console.log('Changed');
        console.log('Old: '+oldValue);
        console.log('New: '+newValue);
    });
    $timeout(function(){       
        $scope.handle='newtweeterhandle';
        console.log("scope Changed");          
       
    },3000);

    $scope.characters=5;
    $scope.rules=[
    {"ruleName":"Must be 5 characters"},
    {"ruleName":"Must not be used elsewhere"},
    {"ruleName":"Must be cool"},
    ];
    console.log($scope.rules);
    $scope.alertClick=function(){
        alert("Clicked!")
    }

    // setTimeout(function(){
    //     $scope.$apply(function(){
    //     $scope.handle='newtweeterhandle';
    //     console.log("scope Changed");
            
    //     });
    // },3000);















    /**$scope.understand = "Introduction to angularJs";
    // $scope.inputValue="";

    $scope.selectPerson = 0;
    $scope.selectGenre = null;
    $scope.people = [
        { id: 0, name: 'Leon', music: ['Rock', 'Metal', 'Dubstep', 'Electro'] },
        { id: 1, name: 'Chris', music: ['Indie', 'Drumstep', 'Dubstep', 'Electro'] },
        { id: 2, name: 'Harry', music: ['Rock', 'Metal', 'Thrash Metal', 'Heavy Metal'] },
        { id: 3, name: 'Allyce', music: ['Pop', 'RnB', 'Hip Hop'] }
    ];

    $scope.singers = [
        { id: 0, name: 'Leon', music: ['Rock', 'Metal', 'Dubstep', 'Electro'], live: true },
        { id: 1, name: 'Chris', music: ['Indie', 'Drumstep', 'Dubstep', 'Electro'], live: true },
        { id: 2, name: 'Harry', music: ['Rock', 'Metal', 'Thrash Metal', 'Heavy Metal'], live: false },
        { id: 3, name: 'Allyce', music: ['Pop', 'RnB', 'Hip Hop'], live: true }
    ];
    $scope.newPerson = null;
    $scope.addNew = function() {
        if ($scope.newPerson != null && $scope.newPerson != "") {
            $scope.singers.push({ id: $scope.people.length, name: $scope.newPerson, live: true, music: [] });
        }
    }
console.log($resource); **/
}]);
