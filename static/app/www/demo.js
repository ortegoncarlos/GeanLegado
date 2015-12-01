// 
// Here is how to define your module 
// has dependent on mobile-angular-ui

var app = angular.module('MobileAngularUiExamples', [
  'ngRoute',
  'mobile-angular-ui',
  
  'mobile-angular-ui.gestures',
  'ngMap'
]);

app.run(function($transform) {
  window.$transform = $transform;
});


app.config(function($routeProvider) {
  $routeProvider.when('/',              {templateUrl: 'home.html', reloadOnSearch: false});
  $routeProvider.when('/perfil',        {templateUrl: 'scroll.html', reloadOnSearch: false}); 
  
  $routeProvider.when('/peril/:id',     {templateUrl: 'tabs.html', reloadOnSearch: false}); 
  
  $routeProvider.when('/forms',         {templateUrl: 'forms.html', reloadOnSearch: false});

  $routeProvider.when('/mapa',         {templateUrl: 'swipe.html', reloadOnSearch: false});
 
  $routeProvider.when('/scanner',      {templateUrl: 'scanner.html', reloadOnSearch: false});
});



//
// For this trivial demo we have just a unique MainController 
// for everything
//
app.controller('MainController', function($rootScope, $scope, $http, $routeParams){
 $scope.web = "http://gl.pulsar.la"
  $scope.swiped = function(direction) {
    alert('Swiped ' + direction);
  };

  // User agent displayed in home page
  $scope.userAgent = navigator.userAgent;
  
  // Needed for the loading screen
  $rootScope.$on('$routeChangeStart', function(){
    $rootScope.loading = true;
  });

  $rootScope.$on('$routeChangeSuccess', function(){
    $rootScope.loading = false;
    $scope.pefilid = $routeParams["id"]
    if ($routeParams) {
        $http.get($scope.web+'/api/pefil/'+$scope.pefilid+'?format=json').
          success(function(data) {
            console.log($scope.pefilid+data)
              $scope.detail = data;
          });

    };
  });


 


  // 
  // 'Scroll' screen
  // 
  

  $http.get($scope.web+'/api/pefil/?format=json').
      success(function(data) {
          $scope.perfil = data;
      });


  //
  // 'Forms' screen
  //  
  $scope.rememberMe = true;
  $scope.email = 'me@example.com';
  
  $scope.login = function() {
    alert('You submitted the login form');
  };



});