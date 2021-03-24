/* 
  Defines all available features and how to calculate them
  Each element in the array requires the format {name:string, calculate:function}
*/
const features = [
  {
    name: "MAV",
    calculate: function (array) {
      let average = array.reduce((a, b) => a + b) / array.length;
      return average;
    },
  },
];
