

//let btn = document.getElementById('saved');
function dropActionyay(){



    let $config = $('#configAction');
    let $checkboxes = $(':checkbox');

    $checkboxes.on('change', function () {
    $('option.dynamic').remove();
    let options = $checkboxes.filter(':checked').map((i, el) => `<option class="dynamic" class="options" value="${el.value}">${el.value}</option>`).get();

    let store = $checkboxes.filter(':checked').map((i, el) => el.value).get();

    $config.append(options);
    //$config.append(store);

    localStorage.setItem("saved-list", options);
    console.log("Test3" + localStorage);
    console.log("Test4" + options);
    }).trigger('change');

}
//btn.addEventListener('click', () => {
//window.location.href = "showData.html";
//})
