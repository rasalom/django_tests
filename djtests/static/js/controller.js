'use strict';

var testsAppController = angular.module('testsAppController', []);

testsAppController.controller('IndexCtrl', ['$scope','$http','$routeParams',
    function($scope,$http, $routeParams) {
        $scope.album = "The Fat Of The Land";

	}]);
