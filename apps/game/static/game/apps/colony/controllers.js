'use strict';

/* Controllers */

var ColonyControllers = angular.module('Colony.controllers', []);

ColonyControllers.controller('ViewController', [ '$scope', '$http', function ($scope, $http) {
	// $scope.ready();
}]);

ColonyControllers.controller('BuildController', [ '$scope', '$http', function ($scope, $http) {
	/*var callbackToken = 'JSON_CALLBACK';
	var url = 'https://gdata.youtube.com/feeds/api/standardfeeds/top_rated?time=today&alt=json&callback=' + callbackToken;
	var timeout = 1;

	$http.jsonp(url).success(function (data) {
		setTimeout(function () {
			var feed = data['feed'];
			var entries = feed['entry'];
			$scope.videos = [];
			for(var i=0;i<entries.length;i++) {
				var entry = entries[i];
				var title = entry['title']['$t'];
				$scope.videos.push({
					title : title
				});
			};
			$scope.ready();
		}, timeout);
	});
*/
}]);

ColonyControllers.controller('ScanController', [ '$scope', '$http', function ($scope, $http) {
	// $scope.ready();
}]);

ColonyControllers.controller('InstallationsController', [ '$scope', 'types', 'building', function ($scope, svcTypes, svcBuilding) {
	$scope.getAvailableInstallations = function () {
		return svcBuilding.availableInstallationsInStation;
	};

	$scope.getType = function (id) {
		return svcTypes.getType(id);
	};

	$scope.activateInstallationTool = function (type_id) {
		console.log('activating tool for \'' + $scope.getType(type_id).label + '\'');
	};
}]);
