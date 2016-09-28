var myApp=angular.module('myTutorial',['ngResource']);
myApp.config(function($interpolateProvider,$httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
    // $resourceProvider.defaults.stripTrailingSlashes = false;
    // $routeProvider.
    //     .when('/',{
    //         templateUrl:"angular",
    //         controller:'mainController'

    //     })
    //     .when('/',{
    //         templateUrl:"spa-ng",
    //         controller:'spaController'

    //     });
/**     $httpProvider.defaults.xsrfCookieName='csrftoken';
    $httpProvider.defaults.xsrfHeaderName='X-CSRFToken';
    $resourceProvider.defaults.stripTrailingSlashes = false; **/
    
