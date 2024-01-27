// 用=将路由参数分割成数组
var idArray = window.location.search.split('=');//idArray=[?id,{{ infornation.user.UID }}]
// 获取路由的参数
var assetId = idArray[1];//assetId={{ infornation.user.UID }}
var uid = document.getElementById("uid");


// $(function(){
//           getData1();
//        });
//function getData1(){
//    $("#id").text(name);
//}

//window.addEventListener("load", function () {
//  window.Notice = function () {
////    uid.value = assetId;
//    uid.focus();
//    document.execcommand('inserttext', false, assetId);
////    uid.innerText = assetId;
////    $("#uid").text(assetId);
//  }
//}, false);

//check.function(){
//    var TTopic = this.$("TTopic").value;
//    var TContent = this.$("TContent").value;
////    var uid = this.$("uid").value;
//    this.$("uid").value = assetId;
//    if(this.trim(uid).length===0){
//        uid = assetId;
//        return false;
//    }
//    else {
//        return true;
//    }
//}

function formS(){
//    var TTopic = document.getElementById("user").value;
//    var TContent = document.getElementById("msg").value;
//    document.getElementById("uid").value = assetId;
    document.getElementById("uid").value = "3";
//    document.getElementById("pustopic").submit();
}