app.directive("weatherReport",function(){
    return {
        restrict:"E",
        templateUrl:'/static/pages/directives/weatherReport.html',
        replace:true,
        scope:{
            weatherDay:'=',
            convertToStandard:"&",
            convertToDate:"&",
            dateFormat:"@"
        }
    }

});

