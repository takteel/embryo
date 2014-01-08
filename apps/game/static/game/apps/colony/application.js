'use strict';

// Declare app level module which depends on filters, and services
var Colony = angular.module('Colony', [
	'ngRoute',
	'Colony.services',
	'Colony.controllers',
	'Colony.filters',
	'Colony.directives'
]);

Colony.config([ '$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
	$routeProvider.when('/', {
		controller : 'ViewController',
		templateUrl : '/static/game/apps/colony/partials/view.html'
	});

	$routeProvider.when('/view', {
		controller : 'ViewController',
		templateUrl : '/static/game/apps/colony/partials/view.html'
	});

	$routeProvider.when('/build', {
		controller : 'BuildController',
		templateUrl : '/static/game/apps/colony/partials/build.html'
	});

	$routeProvider.when('/scan', {
		controller : 'ScanController',
		templateUrl : '/static/game/apps/colony/partials/scan.html'
	});

	$routeProvider.otherwise({
		redirectTo : '/'
	});

	$locationProvider.hashPrefix('!');
}]);

/*
Colony.run(['$rootScope', function ($rootScope) {
	var _getTopScope = function() {
		return $rootScope;
	};

	$rootScope.ready = function () {
		var $scope = _getTopScope();
		$scope.status = 'ready';

		if (!$scope.$$phase) {
			$scope.$apply();
		}
	};

	$rootScope.loading = function () {
		var $scope = _getTopScope();
		$scope.status = 'loading';

		if (!$scope.$$phase) {
			$scope.$apply();
		}
	};

	$rootScope.$on('$routeChangeStart', function () {
		_getTopScope().loading();
	});
}]);
*/
