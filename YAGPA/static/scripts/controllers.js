yagpa.controller('baseCtrl', ['$scope', '$http', '$cookies', function($scope, $http, $cookies) {
	$http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
	$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
	
	$scope.submit = function ($event) {
        $event.preventDefault();
        
        var in_data = 'name=' + $scope.name + 
        	'&shortname=' + $scope.shortname +
        	'&location=' + $scope.location +
        	'&director=' + $scope.director +
        	'&begin_date=' + $scope.begin_date +
        	'&end_date=' + $scope.end_date +
        	'&system=' + $scope.system +
        	'&nb_rounds=' + $scope.nb_rounds;
        
        $http({
            url: '/management/new/',
            method: 'POST',
            data: in_data
        }).success(function(out_data) {
            $scope.response = out_data;
        });
	};
}]);

yagpa.controller('playerCtrl', ['$scope', '$http', function($scope, $http) {
	$scope.player_list = [];
}]);