var tutoApp=angular.module('ngTuto',['ui.bootstrap']);
tutoApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});