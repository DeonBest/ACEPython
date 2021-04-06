# ACE Python 2021

This is the repository for the 2021 Redesign of the ACE software system, used for EMG collection and classification for UNB ECE Department of Biomedical Engineering.

## Background

This project is build with the electron framework. Electron is a framework that is used to built cross-platform desktop applications using web technologies. It combines the chromium rendering engine and the node.js runtime. We have implemented our project with a frontend of HTML, JS, and CSS, and a backend as a python flask api.
Electron: https://www.electronjs.org/docs
Python Flask: https://flask.palletsprojects.com/en/1.1.x/

A basic Electron application needs just these files:

- `package.json` - Points to the app's main file and lists its details and dependencies.
- `main.js` - Starts the app and creates a browser window to render HTML. This is the app's **main process**.
- `index.html` - A web page to render. This is the app's **renderer process**.

You can learn more about each of these components within the [Quick Start Guide](https://electronjs.org/docs/tutorial/quick-start).

## Requirements

To run this application for development you will need the following installations.

To clone and run this repository you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. [Python 3.7](https://www.python.org/downloads/) and Pip3 are required for the python backend.
Versions Used For Development:
NodeJs: v14.13.0
npm: v6.14.9
Python: v3.9.0
Pip: v20.3.1 (Python 3.9)
**From your command line:**

```bash
# Clone this repository
git clone <http://path-to-repo>
# Go into the repository
cd ACEPython
# Install dependencies
npm install
cd backend && pip install -r requirements.txt
# Run the app
npm start
```

Note: If you're using Linux Bash for Windows, [see this guide](https://www.howtogeek.com/261575/how-to-run-graphical-linux-desktop-applications-from-windows-10s-bash-shell/) or use `node` from the command prompt.

## Resources for Learning Electron

- [electronjs.org/docs](https://electronjs.org/docs) - all of Electron's documentation
- [electronjs.org/community#boilerplates](https://electronjs.org/community#boilerplates) - sample starter apps created by the community
- [electron/electron-quick-start](https://github.com/electron/electron-quick-start) - a very basic starter Electron app
- [electron/simple-samples](https://github.com/electron/simple-samples) - small applications with ideas for taking them further
- [electron/electron-api-demos](https://github.com/electron/electron-api-demos) - an Electron app that teaches you how to use Electron
- [hokein/electron-sample-apps](https://github.com/hokein/electron-sample-apps) - small demo apps for the various Electron APIs

## Frontend

As mentioned the frontend is a standard HTML, JS, CSS application. It is structured similar to a website, and is rendered with the chromium rendering engine. The UI elements are divided into components and pages. Pages are the highest level HTML files that represent an entire use case or functionality. They are the main pages/tabs. Components are smaller, more specific HTML snippets that are loaded into the pages and can be reused around the application, for example the NavBar. Bootstrap has been imported for UI elements, the documentation can be found below. Other styles can be applied as standard CSS from files or inline.

Bootstrap: https://getbootstrap.com/docs/5.0/getting-started/introduction/

```
frontend
└───components
│		|- HTML snippets loaded into pages
└───images
|   	|- Images of the actions
└───javascript
|   	|-features
└───pages
|    	|- Tabs/Main Pages
└───styles
		|- Styles loaded into pages

```

## Backend

The backend is a python flask api hosted locally on port 5000. It starts running automatically when the application starts. The api will therefore only be accessed one client at time, the application that is launched.
The api defines standard HTTP endpoints that trigger the respective python function to run. The frontend makes calls to http:// 127.0.0.1:5000 / {endpoint} and handles the data response in javascript, so the response must be in JSON format.

The flask application which defines the endpoints is in backend/engine.py. These endpoints are used to get the list of available data files, readers, actions, getting data being read from a device, etc.

```
backend
└───actions
│		|- .csv file serving as the list of actions
└───data
│		|- .csv data files of emg data that can be used as input
└───readers
|       |- Reader classes for different hardware/sources
└───engine.py - Flask Application defining the endpoints
|
└───requirements.txt - List of python libraries required to be installed

```

## Readers

Readers are the classes that are used to interface with different hardware or input sources. They all implement the abstract class, Reader.py. Adding a new reader can be done by creating a new reader class, and adding the reader to the dict at the top of the engine.py file at a given key. The readers are then requested by the frontend and contain their key and a name which is used for the dropdown field selection. When collection is triggered, the reading will be done from the reader specified with the key. There are two types of readers, the file reader and the data acquisition readers (DAQ). An init() function is called before the first call to the API, and the readers are initialized. The frontend will then trigger start() collect() and stop() to retreive data from the specified device.

## Features

Features are defined in the frontend/javascript directory. The objects contain a name for use in the dropdown, and a calculate function, used to compute the feature on an array of values.

## Data Files

Data files that can be used as input can be stored in backend/data. They must be in a .csv format. The frontend requests the list of files, and allows selection of a file to use if desired.

## Actions

The list of actions is determined from the actions csv file in /backend/actions. The entries need corresponding images in the frontend/images/actions directory. To add an action, simply add an image to the directory and add its file name to the csv. The name that will be displayed in the dropdown will pulled from the file name, so keep naming consistent.

## Debugging

To debug the frontend, you can open chromium dev tools window. In main.js, mainWindow.webContents.openDevTools() opens the window, but only if you are running the application locally without it being bundled into a standalone application. If the backend has been built and pyenginedist folder is present in /backend, it will use the bundled API and considers this the released standalone version. If the application has been built already, you can delete the pyenginedist folder and it will run application under development. You can then use the dev tools window to see console logs, inspect elements, etc.

To debug the backend, you can run `cd backend && python engine.py` to run the API in a terminal window before starting the application with `npm start`. All output from the python execution can be visible with from that terminal window. Once its running, you can also use any other script or postman to hit localhost:5000/ to test.

## Building

To build a standalone Desktop app for this project.
Note: The backend must be built before the frontend. Building the electron app must have a built version of the backend to use for the standalone application.

```bash
# Build the backend
 #Windows
  npm run build-backend-windows
 #Mac
  npm run build-backend-mac
# Build the frontend
  npm run build-frontend
```

The backend is built by [pyinstaller](https://www.pyinstaller.org/) and stored in backend/pyenginedist
The frontend is built by [electron-packager](https://github.com/electron/electron-packager) and stored in the root directory at ace-darwin-x64 (mac) and ace-win32-x64(windows). The respective executable is found inside.

NOTE: Once the backend is built in your directory (pyenginedist exists), it will use that bundled version as the backend. To run local API for development purposes, delete the packaged backend (pyenginedist). The packaging process will also create a folder /backend/build and a file /backend/engine.spec. These can be deleted. 
