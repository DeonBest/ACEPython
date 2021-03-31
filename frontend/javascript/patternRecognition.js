

    var appdata={trials:[]};
    var collectionConfig={
      duration:5,
      delay:5,
      trials:1,
      actions:[]
    };

    $(function () {
      $('#patternRecContainer').load("./dataCollection.html")
    });

    function onTabChange(tab){
      $( "a[class|='nav-link active']" ).toggleClass('active');
      $(`#${tab}Tab`)
            .toggleClass("active")

      $('#patternRecContainer').load(`./${tab}.html`);
    };

    const onOpenPrompt = () => {
    const remote = require("electron").remote;
    const BrowserWindow = remote.BrowserWindow;
    promptWindow = new BrowserWindow({
      height: 600,
      width: 800,
    });
    console.log(__dirname)
    promptWindow.loadFile(__dirname + "/../actionPrompt.html");
    promptWindow.webContents.openDevTools();
//    console.log("testing" + collectionConfig.actions);
  };

