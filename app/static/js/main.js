var app = angular.module("myApp", []);
app.controller("myCtrl", function ($scope, $http) {
    var base_url = "http://localhost:8080"
    $scope.listofchoices = ["Patient", "Specialist"];
    $scope.listofspecialists = ["Name1", "Name2"];

    $scope.GetSchedule = function () {

        var result;
        var url = base_url + "/api/event"
        console.log(url);
        var params = { pid: "2", sid: "2" }
        $http({
            url: url,
            method: "GET",
            params: params
        }).then(response => {
            console.log(response.data);
        });

    }
});

