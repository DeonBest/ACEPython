/*
    Handle toggling of the enabled channels
*/
function onChannelToggle(channel) {
  switch (channel) {
    case "all":
      if ($(`#qc-channel-all`).attr("active") === "true") {
        console.log("all true");
        $("button[id^='qc-channel-']").removeClass("btn btn-primary");
        $("button[id^='qc-channel-']").addClass("btn btn-secondary");
        $("button[id^='qc-channel-']").attr("active", "false");
      } else {
        console.log("all false");
        $("button[id^='qc-channel-']").removeClass("btn btn-secondary");
        $("button[id^='qc-channel-']").addClass("btn btn-primary");
        $("button[id^='qc-channel-']").attr("active", "true");
      }
      break;
    default:
      if ($(`#qc-channel-${channel}`).attr("active") === "true") {
        $(`#qc-channel-${channel}`)
          .toggleClass("btn btn-primary")
          .toggleClass("btn btn-secondary")
          .attr("active", "false");
      } else {
        $(`#qc-channel-${channel}`)
          .toggleClass("btn btn-primary")
          .toggleClass("btn btn-secondary")
          .attr("active", "true");
      }
      break;
  }
}
