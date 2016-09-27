/ Resources have the following methods by default:
// get(), query(), save(), remove(), delete()

angular.module('webTweetsApp.services', ['ngResource'])
  .factory('Tweet', function($resource) {
    return $resource('/api/tweets/:id/'); 
  })
  .factory('User', function($resource) {
    return $resource('/api/users/:id/'); 
});