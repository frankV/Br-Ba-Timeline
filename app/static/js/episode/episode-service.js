'use strict';

angular.module('bb.timeline')
  .factory('Episode', ['$resource', function ($resource) {
    return $resource('bb.timeline/episodes/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
