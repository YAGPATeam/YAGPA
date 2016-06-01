var yagpa = angular.module('yagpa', ['djng.forms']).config(function($httpProvider) { //, ['ngRoute']
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

/*
 * .config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
}).
 */
/*
app.config(['$routeProvider',
  	function($routeProvider) {
	    $routeProvider.
		    when('/', {
		        templateUrl: '../templates/base.html',
		        controller: 'baseCtrl'
		    }).
		    when('/management', {
		        templateUrl: './app/views/base.html',
		        controller: 'baseCtrl'
		    }).
		    otherwise({
		        redirectTo: '/'
		    });
    }]);
*/