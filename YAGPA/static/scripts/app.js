var yagpa = angular.module('yagpa', ['djng.forms', 'ngCookies']).config(function($httpProvider) { //, ['ngRoute']
	$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
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