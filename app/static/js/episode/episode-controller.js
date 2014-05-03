'use strict';

angular.module('bb.timeline')
  .controller('EpisodeController', ['$scope', '$modal', 'resolvedEpisode', 'Episode',
    function ($scope, $modal, resolvedEpisode, Episode) {

      $scope.episodes = resolvedEpisode;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.episode = Episode.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Episode.delete({id: id},
          function () {
            $scope.episodes = Episode.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Episode.update({id: id}, $scope.episode,
            function () {
              $scope.episodes = Episode.query();
              $scope.clear();
            });
        } else {
          Episode.save($scope.episode,
            function () {
              $scope.episodes = Episode.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.episode = {
          
          "season": "",
          
          "number": "",
          
          "title": "",
          
          "released": "",
          
          "duration": "",
          
          "rating": "",
          
          "summary": "",
          
          "storyline": "",
          
          "photos": "",
          
          "keywords": "",
          
          "quote": "",
          
          "director": "",
          
          "writer": "",
          
          "calendar_start": "",
          
          "calendar_end": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var episodeSave = $modal.open({
          templateUrl: 'episode-save.html',
          controller: EpisodeSaveController,
          resolve: {
            episode: function () {
              return $scope.episode;
            }
          }
        });

        episodeSave.result.then(function (entity) {
          $scope.episode = entity;
          $scope.save(id);
        });
      };
    }]);

var EpisodeSaveController =
  function ($scope, $modalInstance, episode) {
    $scope.episode = episode;

    
    $scope.releasedDateOptions = {
      dateFormat: 'yy-mm-dd',
      
      
    };
    $scope.calendar_startDateOptions = {
      dateFormat: 'yy-mm-dd',
      
      
    };
    $scope.calendar_endDateOptions = {
      dateFormat: 'yy-mm-dd',
      
      
    };

    $scope.ok = function () {
      $modalInstance.close($scope.episode);
    };

    $scope.cancel = function () {
      $modalInstance.dismiss('cancel');
    };
  };
