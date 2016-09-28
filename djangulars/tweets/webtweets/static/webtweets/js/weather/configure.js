// configuring routing.
app.config(function($routeProvider, $locationProvider,$interpolateProvider, $httpProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $locationProvider.html5Mode({ enabled:true,requireBase: false});
    $routeProvider
        .when('/', { // If URL is at /, uses template at
            templateUrl: '/static/pages/weather/home.html', // this location
            controller: 'homeController' // and apply instructions from this controller
        })
        .when('/forecast/', { // If URL is at /, uses template at
            templateUrl: '/static/pages/weather/forecast.html', // this location
            controller: 'forecastController' // and apply instructions from this controller
        }).when('/forecast/:days', { // If URL is at /, uses template at
            templateUrl: '/static/pages/weather/forecast.html', // this location
            controller: 'forecastController' // and apply instructions from this controller
        })
        .when('/typehead/', { // If URL is at /, uses template at
            templateUrl: '/static/pages/weather/type_head.html', // this location
            controller: 'searchController' // and apply instructions from this controller
        });
});
