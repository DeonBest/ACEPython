function showToast(text) {
  console.log(text);
  $("#toast-text").html(text);
  $(".toast").toast("show");
}
