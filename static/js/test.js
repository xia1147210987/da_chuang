 const signInBtn = document.getElementById("send-my-url-to-django-button");

// $(document).ready(function() {
//    var url = data.result.docs[i].source.enriched.url.url;
//    alert('0');
//    $('#send-my-url-to-django-button').click(function() {
////        alert('1');
//        $.ajax({
//            url: "process_url_from_client",
//            type: "POST",
////            dataType: "json",
//            data: {
//                url: url,
//                csrfmiddlewaretoken: '{{ csrf_token }}'
//            },
//            success : function(json) {
//                alert("Successfully sent the URL to Django");
//            },
//            error : function(xhr,errmsg,err) {
//                alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
//            }
//        });
//    });
//});

signInBtn.addEventListener("click", () => {
    alert('0');
    $.ajax({
            url: "process_url_from_client/",
            type: "POST",
            dataType: "json",
            data: {
                url: 1,
                csrfmiddlewaretoken: '{{ csrf_token }}',
            },
            success: function(response) {
                // unpack response:
                status = response.status
            }
        });
    alert('1');
});