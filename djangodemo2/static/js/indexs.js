const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");

// const fistForm = document.getElementById("form1");
// const secondForm = document.getElementById("form2");

const container = document.querySelector(".container");
var password = document.getElementById('pass');


addEventListener("load", function () {
            setTimeout(hideURLbar, 0);
        }, false);

        function hideURLbar() {
            window.scrollTo(0, 1);
        }

// 页面滑动
signInBtn.addEventListener("click", () => {
	container.classList.remove("right-panel-active");
});

signUpBtn.addEventListener("click", () => {
	container.classList.add("right-panel-active");
});
// 阻止表单数据提交
// fistForm.addEventListener("submit", (e) => e.preventDefault());
// secondForm.addEventListener("submit", (e) => e.preventDefault());

// 密码显示/隐藏
document.getElementById('conceal').addEventListener('click',function(){
    if(password.type==='password')
        {
            password.setAttribute('type','text');
            document.getElementById('conceal').classList.add('yincang');
        }else{
        	password.setAttribute('type','password');
            document.getElementById('conceal').classList.remove('yincang');
        }
});

// 记住密码
$(document).ready(function(){
    var strName = localStorage.getItem('keyName');
    var strPass = localStorage.getItem('keyPass');
    if(strName){
        $('#user').val(strName);
    }if(strPass){
        $('#password').val(strPass);
    }
});
function loginBtn_click(){
    var strName = $('#user').val();
    var strPass = $('#password').val();
    localStorage.setItem('keyName',strName);
    if($('#remember').is(':checked')){
        localStorage.setItem('keyPass',strPass);
    }else{
        localStorage.removeItem('keyPass');
    }
};

// 弹窗提示
//type:1（成功）, 2（失败）, 3（警告）
//time:ms
function displayAlert(type, data, time){
    var tip=document.createElement("div");

      if(type == "1") {
          tip.style.backgroundColor = "#009900";
      } else if(type == "2") {
          tip.style.backgroundColor = "#990000";
      } else if(type == "3") {
          tip.style.backgroundColor = " #e6b800";
      } else {
          console.log("入参type错误");
          return;
      }
          tip.id="tip";
          tip.style.position = "absolute";
          tip.style.width = "300px";
          tip.style.height = "60px";
          tip.style.margin = "0 auto";
          tip.style.left = "40%";
          tip.style.top = "50%";
          tip.style.color = "white";
          tip.style.fontSize = "25px";
          tip.style.borderRadius = "20px";
          tip.style.textAlign="center";
          tip.style.lineHeight="60px";

          if(document.getElementById("tip")==null){
              document.body.appendChild(tip);
              tip.innerHTML=data;
              setTimeout(function(){
                  document.body.removeChild(tip);
              } ,time);
      }
}

//$(document).ready(function(){
//  var cdata = JSON.parse('{{ context|safe }}')
//	var msg = cdata.msg;
//	var tip = cdata.tip;
//	if (msg == "" || tip == "")
//	else displayAlert(tip, msg, 1500);
//});



    function test0() {
        displayAlert("success", "success TEST", 1500);
    }
    function test1() {
        displayAlert("error", "error TEST", 1500);
    }
    function test2() {
        displayAlert("info", "info TEST", 1500);
    }