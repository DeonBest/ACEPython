var data;


//let scrapeJSON = '../../../backend/csvToJS.py'
//$.get(scrapeJSON, function(data) {
//   // Get JSON data from Python script
//   if (data){
//      console.log("Data returned:", data)
//   }
//   jobDataJSON = JSON.parse(data)
//})

async function getData(){
       const response = await fetch('../../../backend/data/emg1KT60.csv');
       const data = await response.text();
       const table = data.split('\n').slice(1);
       let X_value = [];
       table.forEach ( row => {
                 const columns = row.split((','));
                  const year = columns[0];
                  X_value.push(year);

       });
        console.log("This ",X_value);
}


//$.ajax({
//    url: "../../../backend/csvToJS.py",
//    success: callbackFunc
//});
//
//
//function callbackFunc(response) {
//    // do something with the response
//    console.log(response);
//}



//var Papa = require('papaparse');
//var results = [];
//    Papa.parse('../../../backend/data/emg1KT60.csv', {
//        download: true,
//        header: false,
//        complete: function(result){
//            console.log("papa " +JSON.stringify(result.data[0]));
//            results.push(result);
//            console.log(results);
//            console.log(results.length);
//        }
//    });




//var csvFilePath='../../../backend/data/emg1KT60.csv'
//var csv=require('csvtojson')
//csv()
//.fromFile(csvFilePath)
//.then((jsonObj)=>{
//    console.log("cjeiaojcea"+jsonObj);
//    /**
//     * [
//     * 	{a:"1", b:"2", c:"3"},
//     * 	{a:"4", b:"5". c:"6"}
//     * ]
//     */
//})

//const jsonArray=await csv().fromFile(csvFilePath);

