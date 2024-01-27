const logo = document.getElementById('logo');

logo.addEventListener("click", () => {
    var username = document.getElementById("cposter").innerHTML;
    alert(username);
    $.ajax({
        method: 'POST',
        url: "userinf/",
        data: {'username': username},
        success: function (data) {
             //this gets called when server returns an OK response
             alert("it worked!");
        },
        error: function (data) {
             alert("it didnt work");
        }
    });
});
;