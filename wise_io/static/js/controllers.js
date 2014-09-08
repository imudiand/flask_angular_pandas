var phonecatApp = angular.module('wiseioApp', []);
phonecatApp.controller('QueryCtrl', function ($scope, $http) {
  $http.get('query').success(function(data) {
    $scope.rows = data.rows;
    $scope.index_first = data.index_first;
    $scope.index_last = data.index_last;
  });
});