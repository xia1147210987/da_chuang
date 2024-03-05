 // 用=将路由参数分割成数组
var idArray = window.location.search.split('=');//idArray=[?id,{{ infornation.user.UID }}]
// 获取路由的参数
var assetId = idArray[1];//assetId={{ infornation.user.UID }}
 $(document).ready(function() {
//    var url = data.result.docs[i].source.enriched.url.url;
    console.log('用户ID:', assetId)
    $.ajax({
        method: 'POST',
        url: "getuser/", //url设置的调用views函数的路径
        data: {
                'uid':  assetId,
                csrfmiddlewaretoken: '{{ csrf_token }}',
        },
        success: function (data) {
             console.log('后端返回内容:', data)
             document.getElementById("uname").value = data;
             document.getElementById("ID").value = 'ID '+assetId;
        },
        error: function (data) {
            console.log('错误')
        }
    });
});



function save() {
    var context = $("<p>").append($("html").clone()).html();
    var postUrl = "/userinf/";//提交地址
    var postData = context; //第一个数据

    var ExportForm = document.createElement("FORM");
    document.body.appendChild(ExportForm);
    ExportForm.method = "POST";

    var newElement = document.createElement("input");
    newElement.setAttribute("name", "sn");
    newElement.setAttribute("type", "hidden");

    var newElementcsrf = document.createElement("input");
    newElementcsrf.setAttribute("name", "csrfmiddlewaretoken");
    newElementcsrf.setAttribute("type", "hidden")

     var newElementraw = document.createElement("input");
    newElementraw.setAttribute("name", "raw_result");
    newElementraw.setAttribute("type", "hidden")

    ExportForm.appendChild(newElement);
    ExportForm.appendChild(newElementcsrf);
    ExportForm.appendChild(newElementraw);

    newElement.value = postData;
    newElementcsrf.value =  $('#csrf_token').val();//读取隐藏的csrf input标签的value
    newElementraw.value =  $('#raw_result').val();//读取隐藏的raw_result input标签的value

    ExportForm.action = postUrl;
    ExportForm.submit();
};

