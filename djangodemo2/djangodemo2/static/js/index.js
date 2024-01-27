const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");

// const fistForm = document.getElementById("form1");
// const secondForm = document.getElementById("form2");

const container = document.querySelector(".container");
var password = document.getElementById('password');
var anniu = document.getElementById('conceal');

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
anniu.addEventListener('click',function(){
    if(password.type==='password')
        {
            password.setAttribute('type','text');
            anniu.classList.add('yincang');
        }else{
        	password.setAttribute('type','password');
            anniu.classList.remove('yincang');
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
