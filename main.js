// Modules to control application life and create native browser window
const { app, BrowserWindow } = require("electron");
// import {PythonShell} from 'python-shell';
const path = require("path");
const { PythonShell } = require("python-shell");

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow;

const env = process.env.NODE_ENV || "development";

// If development environment
if (env === "development") {
  try {
    require("electron-reload")(__dirname);
  } catch (e) {
    console.log(e);
  }
}
process.env["ELECTRON_DISABLE_SECURITY_WARNINGS"] = "true";
function createWindow() {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    width: 1000,
    height: 800,
    webPreferences: {
      nodeIntegration: true,
      enableRemoteModule: true,
    },
  });

  /*
  PythonShell.run("backend/engine.py", null, function (err) {
    if (err) throw err;
  });
  */

  // and load the index.html of the app.
  mainWindow.loadFile("frontend/pages/quickCollect.html");

  // Open the DevTools.
  mainWindow.webContents.openDevTools();

  // Emitted when the window is closed.
  mainWindow.on("closed", function () {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    mainWindow = null;
  });
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
//app.on("ready", createWindow);

// Quit when all windows are closed.
app.on("window-all-closed", function () {
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", function () {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) {
    createWindow();
  }
});

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
// add these to the end or middle of main.js

let pyProc = null;
let pyPort = null;

function selectPort() {
  pyPort = 5000;
  return pyPort;
}

function createPyProc() {
  let script = getScriptPath();
  let port = "" + selectPort();

  if (guessPackaged()) {
    pyProc = require("child_process").execFile(script, [port]);
  } else {
    //pyProc = require('child_process').spawn('python', [script, port])
    PythonShell.run("backend/engine.py", null, function (err) {
      if (err) throw err;
    });
  }

  if (pyProc != null) {
    console.log("child process success on port " + port);
  }

  createWindow();
}

function exitPyProc() {
  pyProc.kill();
  pyProc = null;
  pyPort = null;
}

app.on("ready", createPyProc);
app.on("will-quit", exitPyProc);

const PY_DIST_FOLDER = "backend/pyenginedist";
const PY_FOLDER = "backend";
const PY_MODULE = "engine"; // without .py suffix

function guessPackaged() {
  const fullPath = path.join(__dirname, PY_DIST_FOLDER);
  return require("fs").existsSync(fullPath);
}

function getScriptPath() {
  if (!guessPackaged()) {
    return path.join(__dirname, PY_FOLDER, PY_MODULE + ".py");
  }
  if (process.platform === "win32") {
    return path.join(__dirname, PY_DIST_FOLDER, PY_MODULE, PY_MODULE + ".exe");
  }
  return path.join(__dirname, PY_DIST_FOLDER, PY_MODULE, PY_MODULE);
}
