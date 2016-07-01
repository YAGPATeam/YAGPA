yagpa.controller('baseCtrl', ['$scope', '$http', '$cookies', function($scope, $http, $cookies) {
	$http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
	$http.defaults.headers.post['X-CSRFToken'] = $cookies.get('csrftoken');
}]);

yagpa.controller('formNewTournamentCtrl', ['$scope', '$http', '$cookies', function($scope, $http, $cookies) {
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
        }).success(function (data, status, headers, config) {
        	
        }).error(function (data, status, header, config) {
        	
        });
	};
}]);

yagpa.controller('formLoginCtrl', ['$scope', '$http', function($scope, $http) {
	$scope.submit = function ($event) {
        $event.preventDefault();

        var in_data = 'username=' + $scope.username + 
        	'&password=' + $scope.password;
        
        $http({
            url: '/auth/login/',
            method: 'POST',
            data: in_data
        }).success(function (data, status, headers, config) {
        	/*scope.$apply(function() { 
        		   $location.path("/management/my_tournaments/"); 
        		});*/
        }).error(function (data, status, header, config) {
        	
        });
        
	};
}]);

yagpa.controller('playerCtrl', ['$scope', '$http', function($scope, $http) {
	$scope.list_players = [{'agaExpirationDate': '','agaId':'','club':'56Lo','country':'FR','egfPin':'','ffgLicence':'','ffgLicenceStatus':'','firstName':'Damien','grade':'13K','name':'le_Goff','participating':'11111111111111111111','rank':'13K','rating':'800','ratingOrigin':'INI','registeringStatus':'FIN','smmsCorrection':'0'},
		{'agaExpirationDate': '','agaId':'','club':'56Lo','country':'FR','egfPin':'','ffgLicence':'0634006','ffgLicenceStatus':'L','firstName':'Alexis','grade':'1K','name':'Thaumoux','participating':'11111111111111111111','rank':'1K','rating':'1985','ratingOrigin':'FFG','registeringStatus':'FIN','smmsCorrection':'0'},
		{'agaExpirationDate': '','agaId':'','club':'56Lo','country':'FR','egfPin':'','ffgLicence':'1300090','ffgLicenceStatus':'L','firstName':'Ronan','grade':'8K','name':'Delasnerie','participating':'11111111111111111111','rank':'8K','rating':'1318','ratingOrigin':'FFG','registeringStatus':'FIN','smmsCorrection':'0'},
		{'agaExpirationDate': '','agaId':'','club':'56Lo','country':'FR','egfPin':'','ffgLicence':'1200322','ffgLicenceStatus':'L','firstName':'Benjamin','grade':'9K','name':'Saulnier','participating':'11111111111111111111','rank':'9K','rating':'1171','ratingOrigin':'FFG','registeringStatus':'FIN','smmsCorrection':'0'},
		{'agaExpirationDate': '','agaId':'','club':'56Lo','country':'FR','egfPin':'','ffgLicence':'0534001','ffgLicenceStatus':'L','firstName':'Maël','grade':'1D','name':'Rabasse','participating':'11111111111111111111','rank':'1D','rating':'2123','ratingOrigin':'FFG','registeringStatus':'FIN','smmsCorrection':'0'},
		{'agaExpirationDate': '','agaId':'','club':'56Lo','country':'FR','egfPin':'','ffgLicence':'0634001','ffgLicenceStatus':'L','firstName':'Mathieu','grade':'3D','name':'Delli-Zotti','participating':'11111111111111111111','rank':'3D','rating':'2318','ratingOrigin':'FFG','registeringStatus':'FIN','smmsCorrection':'0'}];
	
	$scope.list_tournament_players = [];
	// $scope.list_players = $scope.data;
	
	$scope.register = function(player) {
		$scope.list_tournament_players.push(player);
	};
}]);