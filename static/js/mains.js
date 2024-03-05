const logo = document.getElementById('logo');
//var z = document.getElementsByClassName("contents--brown");
//var h = document.getElementsByClassName("contents--black");

//logo.addEventListener("click", () => {
//    var username = document.getElementById("Usname").innerHTML;
//    $.ajax({
//        method: 'POST',
//        url: "userinf/",
//        data: {
//                'username': username,
//                csrfmiddlewaretoken: '{{ csrf_token }}',
//        },
//        success: function (data) {
//             location.replace("pmain/?username=" + data);
//        },
//        error: function (data) {
//            console.log('错误')
//        }
//    });
//});

//    const logo = document.getElementById('logo');
//    var idArray = window.location.search.split('=');
//    var assetId = idArray[1];
//    const post = document.getElementById('post');
//    $(document).ready(function() {
//        console.log('用户ID:', assetId)
//        $.ajax({
//            method: 'POST',
//            url: "getuser/",
//            data: {
//                    'uid':  assetId,
//                    csrfmiddlewaretoken: '{{ csrf_token }}',
//            },
//            success: function (data) {
//                 console.log('后端返回内容:', data)
//                 document.getElementById("uname").innerHTML = assetId;
//                 document.getElementById("ID").innerHTML = "ID "+data;
//            },
//            error: function (data) {
//                console.log('错误')
//            }
//        });
//    });

