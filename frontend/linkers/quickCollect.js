let { PythonShell } = require("python-shell");
var path = require("path");

function getDataFiles() {
  var options = {
    scriptPath: path.join(__dirname, "../../backend/"),
    args: [],
    mode: "json",
  };

  let pyshell = new PythonShell("get_data_files.py", options);

  pyshell.on("message", function (data_files) {
    for (i = 0; i < data_files.length; i++) {
      const split = data_files[i].split("/");
      file_name = split[split.length - 1];
      $("#file-select").append(
        $("<option>", {
          value: data_files[i],
          text: file_name,
        })
      );
    }
  });
}

function getCSVData() {
  const file = $("#file-select option:selected").val();
  console.log("F", file);
  var options = {
    scriptPath: path.join(__dirname, "../../backend/"),
    args: [file],
    mode: "json",
  };

  let pyshell = new PythonShell("get_csv_data.py", options);

  pyshell.on("message", function (message) {
    console.log("M", message);
    return "test";
  });

  pyshell.end();
}

function onFileSelect() {
  //set radio to file and enable the file selector
  $("#file-select").attr("disabled", false);
  $("#input-type-live").attr("checked", false);
}

function onLiveSelect() {
  //set radio to live and disable the file selector
  $("#file-select").attr("disabled", true);
  $("#input-type-file").attr("checked", false);
}
