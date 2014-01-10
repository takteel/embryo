'use strict';

/* Services */

var module = angular.module('Colony.services', []);

module.service('building', [ '$rootScope', function (rootScope) {
	var service = {
		
	};

	return service;
}]);

module.service('types', [ '$rootScope', function (rootScope) {
	this.types = {
		0: {
			icon: 'CC',
			label: 'command center'
		},
		1: {
			icon: 'EX',
			label: 'ore exctractor'
		},
		2: {
			icon: 'RF',
			label: 'ore refinery'
		},
	};

	this.getType = function (id) {
		return (id in this.types) ? this.types[id] : undefined;
	};
}]);

module.service('building', [ '$rootScope', function (rootScope) {
	this.availableInstallationsInStation = [
		{ type_id: 0, count: 2 },
		{ type_id: 1, count: 10 },
		{ type_id: 2, count: 6 }
	];

	this.changesList = [
		{ type_id: 0 },
		{ type_id: 1 },
		{ type_id: 2 }
	];
}]);
