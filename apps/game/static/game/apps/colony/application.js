'use strict';

// Declare app level module which depends on filters, and services
var app = angular.module('Colony', [
	'ngRoute',
	'Colony.services',
	'Colony.controllers',
	'Colony.filters',
	'Colony.directives'
]);

app.constant('settings', {
	partialsUrl: '/static/game/apps/colony/partials'
});

app.config([ '$routeProvider', '$locationProvider', 'settings' , function ($routeProvider, $locationProvider, settings) {
	$routeProvider.when('/', {
		controller : 'ViewController',
		templateUrl : settings.partialsUrl + '/view.html'
	});

	$routeProvider.when('/view', {
		controller : 'ViewController',
		templateUrl : settings.partialsUrl + '/view.html'
	});

	$routeProvider.when('/build', {
		controller : 'BuildController',
		templateUrl : settings.partialsUrl + '/build.html'
	});

	$routeProvider.when('/scan', {
		controller : 'ScanController',
		templateUrl : settings.partialsUrl + '/scan.html'
	});

	$routeProvider.otherwise({
		redirectTo : '/'
	});

	$locationProvider.hashPrefix('!');
}]);

/*
app.run(['$rootScope', function ($rootScope) {
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
