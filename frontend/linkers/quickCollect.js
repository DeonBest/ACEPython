let { PythonShell } = require("python-shell");
var path = require("path");

function getDataFiles(){
  var options = {
    scriptPath: path.join(__dirname, "../../backend/"),
    args: [],
  };

  let pyshell = new PythonShell("get_data_files.py", options);


  pyshell.on("message", function (message) {
    //Python returns string with ', must parse string into array with "
    let data_files = message.replace(/'/g, '"');
    data_files = JSON.parse(data_files)
    for(i=0;i<data_files.length;i++){
      const split = data_files[i].split('/')
      file_name = split[split.length-1]
      $('#file-select').append($('<option>', { 
          value: data_files[i],
          text : file_name
      }));
    }

  });
}

function onFileSelect(){
  //set radio to file and enable the file selector
  $('#file-select').attr('disabled', false)
  $('#input-type-live').attr('checked', false)
}

function onLiveSelect(){
  //set radio to live and disable the file selector
  $('#file-select').attr('disabled', true)
  $('#input-type-file').attr('checked', false)
}