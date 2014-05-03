'use strict';

angular.module('bb.timeline')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/episodes', {
        templateUrl: 'views/episode/episodes.html',
        controller: 'EpisodeController',
        resolve:{
          resolvedEpisode: ['Episode', function (Episode) {
            return Episode.query();
          }]
        }
      })
    }]);
