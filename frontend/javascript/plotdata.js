var actionNum=5;
var actionInterval = 600;
var emgfile = 'emg1KT60.csv'
const channel1Data = '../../../backend/data/emg1KT60.csv'
const channel2Data = '../../../backend/data/emg1KT120.csv'
/*
const channel3Data = ',,,'
         to
const channel8Data = ',,,'
*/
/*read csv to array*/
//var totalData = []
async function getData1(){
    try{


   const response = await fetch(channel1Data);
   const data = await response.text();
   const table = data.split('\n').slice(1);
   let X_value = [];
   table.forEach ( row => {
             const columns = row.split((','));
              const year = columns[0];
              X_value.push(year);

   });
   return X_value;
   }catch(error){
    console.log(error);
   }
}
async function getData2(){
    try{


   const response = await fetch(channel2Data);
   const data = await response.text();
   const table = data.split('\n').slice(1);
   let X_value = [];
   table.forEach ( row => {
             const columns = row.split((','));
              const year = columns[0];
              X_value.push(year);

   });
   return X_value;
   }catch(error){
    console.log(error);
   }
}


//getData().then(a=>console.log(a.keys()));

//getData().then(function(a){=>totalData.push(a));

//console.log("Test",totalData);



var csv = require('csv-parser');
var fs = require('fs');
//var results = [];
//var $savedItems = localStorage.getItem('saved-list')
//var totalData = $savedItems.split(',');
var actionsChannel1=[];
var actionsChannel2=[];
//var data1 = csvtoarray();


async function drawChartChannel1(){
    var thing1 = await splitDataByActionChannel1(actionInterval,actionNum);

    //var samplesize=totalData.length;
    var samplesize=actionsChannel1[0].length;

    //var chartdata= totalData.slice(0,1000); //if interval per action is 200 samples
    var chartdata = actionsChannel1[0];
    console.log(chartdata);
    var xaxis= Array.from({length: chartdata.length}, (_, index) => index + 1);


    var ctxL = document.getElementById("chartReview1").getContext('2d');
    var myLineChart = new Chart(ctxL, {
        type: 'line',
        data: {
          labels: xaxis,
          datasets: [{
              label: "My First dataset",
              data: chartdata,
              backgroundColor: [
                'rgba(0, 0, 0, 0)',
              ],
              borderColor: [
                'rgba(200, 99, 132, .7)',
              ],
              borderWidth: 2,lineTension: 0,pointRadius:0
            }

          ]
        },
        options: {
          responsive: true,

        }
    });
    console.log("IN funtion",thing);
}

async function drawChartChannel2(){
    var thing2 = await splitDataByActionChannel2(actionInterval,actionNum);

    //var samplesize=totalData.length;
    var samplesize=actionsChannel2[0].length;

    //var chartdata= totalData.slice(0,1000); //if interval per action is 200 samples
    var chartdata = actionsChannel2[0];
    console.log(chartdata);
    var xaxis= Array.from({length: chartdata.length}, (_, index) => index + 1);


    var ctxL = document.getElementById("chartReview2").getContext('2d');
    var myLineChart = new Chart(ctxL, {
        type: 'line',
        data: {
          labels: xaxis,
          datasets: [{
              label: "My second dataset",
              data: chartdata,
              backgroundColor: [
                'rgba(0, 0, 0, 0)',
              ],
              borderColor: [
                'rgba(20, 99, 132, .7)',
              ],
              borderWidth: 2,lineTension: 0,pointRadius:0
            }

          ]
        },
        options: {
          responsive: true,

        }
    });
    console.log("IN funtion",thing);
}
//function csvtoarray(){
//var resultplz;
//
//    fs.createReadStream('../../../../ACEPython/backend/data/'+emgfile)
//      .pipe(csv())
//      .on('data', (data) => results.push(Object.values(data)[0]))
//      .on('end', () => {
//        localStorage.setItem("saved-list",results);
//        resultplz = results;
//        return results;
//
//      });
//console.log("value"+results);
//console.log("value2"+resultplz);
//
//}


async function splitDataByActionChannel1(size,numAction){
//split total data by the number of actions in the data. If there are 10 actions in the data,
//this function will split the data by 10 individual data.
    var something = await getData1();
    var dataSizePerAction = size;
    var dataOfAction;// = totalData.slice(0,dataSizePerAction);
    var sliceFrom;
    var sliceTo;
    for (var i=0;i<numAction;i++){
        sliceFrom = (i*(dataSizePerAction+1));
        sliceTo = sliceFrom+dataSizePerAction;
        dataOfAction = something.slice(sliceFrom,sliceTo);
        actionsChannel1[i] = dataOfAction;
    }
    return actionsChannel1;

}
async function splitDataByActionChannel2(size,numAction){
//split total data by the number of actions in the data. If there are 10 actions in the data,
//this function will split the data by 10 individual data.
    var something = await getData2();
    var dataSizePerAction = size;
    var dataOfAction;// = totalData.slice(0,dataSizePerAction);
    var sliceFrom;
    var sliceTo;
    for (var i=0;i<numAction;i++){
        sliceFrom = (i*(dataSizePerAction+1));
        sliceTo = sliceFrom+dataSizePerAction;
        dataOfAction = something.slice(sliceFrom,sliceTo);
        actionsChannel2[i] = dataOfAction;
    }
    return actionsChannel2;

}


//console.log("data"+results);
//console.log("value"+results);
//console.log("size is" + samplesize);







//console.log("data"+xaxis);
//splitDataByAction(5,10);

//console.log("created "+actions[0]);