const features = [
  {
    name: "MAV",
    calculate: function (array) {
      let average = array.reduce((a, b) => a + b) / array.length;
      return average;
    },
  },
];
