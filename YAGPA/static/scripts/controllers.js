<<<<<<< refs/remotes/origin/master
yagpa.controller('baseCtrl', ['$scope', '$http', function($scope, $http) {
	$scope.submit = function ($event) {
        $event.preventDefault();
        
        $http({
            url: '/new',
            method: 'POST',
            data: in_data 
        }).success(function(out_data) {
            $scope.response = out_data;
        });
	};
}]);

yagpa.controller('playerCtrl', ['$scope', '$http', function($scope, $http) {
	$scope.player_list = [];
=======
yagpa.controller('baseCtrl', ['$scope', '$http', function($scope, $http) {
	$scope.submit = function ($event) {
        $event.preventDefault();
        
        $http({
            url: '/new',
            method: 'POST',
            data: in_data 
        }).success(function(out_data) {
            $scope.response = out_data;
        });
	};
}]);

yagpa.controller('playerCtrl', ['$scope', '$http', function($scope, $http) {
	$scope.player_list = [];
>>>>>>> ok
}]);