'use strict';

var testsApp = angular.module('testsApp', [
  'ngRoute',
  'testsAppController',
]);


testsApp.config(['$routeProvider','$locationProvider',
  function($routeProvider, $locationProvider) {

	//$locationProvider.html5Mode(true);

    $routeProvider.
      when('/albums', {
          template: '<p>{{ album }}</p>',
          controller: 'IndexCtrl',
          label: "Start"
        }).
      otherwise({
        redirectTo: '/',
        label: "Start",
        template: '<p>Angular JS Works</p>',
        controller: 'IndexCtrl',
      });
  }]);