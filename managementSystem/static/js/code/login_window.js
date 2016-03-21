/**
 * Created by 香菇 on 2016/1/12.
 */


//获取窗口的高度
var windowHeight;
//获取窗口的宽度
var windowWidth;
//获取弹窗的宽度
var popWidth;
//获取弹窗高度
var popHeight;
function init(){
    windowHeight=$(window).height();
    windowWidth=$(window).width();
    popHeight=$(".window").height();
    popWidth=$(".window").width();
}
$(document).ready(function () {
    $("#loginBut").click(function () {
        poploginWindow();
    });
    $("#registerBut").click(function () {
        popregisterWindow();
    });
});
function closeWindow(){
    $(".title img").click(function(){
        $(this).parent().parent().hide("slow");
    });
}
function poploginWindow(){
    init();
    //计算弹出窗口的左上角Y的偏移量
    var popY=(windowHeight-popHeight)/2;
    var popX=(windowWidth-popWidth)/2;
    $("#login").css("top",popY).css("left",popX).slideToggle("slow");
    closeWindow();
}
function popregisterWindow(){
    init();
    //计算弹出窗口的左上角Y的偏移量
    var popY=(windowHeight-popHeight)/2;
    var popX=(windowWidth-popWidth)/2;
    $("#reg_Box").css("top",popY).css("left",popX).slideToggle("slow");
    closeWindow();
}

function sendform(){
    $.ajax({
        cache: false,
        type: "POST",
        url:"login",	//把表单数据发送到ajax.jsp、
        data:$('#ajaxFor').serialize(),	//要发送的是ajaxFrm表单中的数据
        async: false,
        error: function(request) {
            alert("登录失败o(>﹏<)o了");
        },
        success: function(data) {
            var jsonObj = JSON.parse(data);
            if (jsonObj.Success){
                //登录成功， 跳转网页
                window.location.href="/";
            }else{
                //否则显示错误信息
                $("#redata").html(jsonObj.html);
            }

        }
    });
}

function sendreg(){
    var userName = $("#register_input_2 input").val();
    var pass_1 = $("#register_input_3 input").val();
    var pass_2 = $("#register_input_4 input").val();
    if (userName == ""){
        $("#register_error_2").html("<ul class='errorlist'><li>请输入用户名</li></ul>");
        return ;
    }else{
        $("#register_error_2").html("");
    }
    if (pass_1 == ""){
        $("#register_error_3").html("<ul class='errorlist'><li>请输入登录密码</li></ul>");
        if (pass_2 == ""){
            $("#register_error_4").html("<ul class='errorlist'><li>请再次输入密码</li></ul>");
        }else{
            $("#register_error_4").html("");
        }
        return ;
    }else{
        $("#register_error_3").html("");
    }
    if (pass_1.length < 6){$("#register_error_3").html("<ul class='errorlist'><li>密码长度不能小于6位</li></ul>");return ;}
    else{$("#register_error_3").html("");}
    if (pass_1 != pass_2){
        $("#register_error_4").html("<ul class='errorlist'><li>两次输入不一致</li></ul>");
        return ;
    }else{
        $("#register_error_4").html("");
        $("#register_input_4 input").val(hex_md5(pass_2));
        $("#register_input_3 input").val(hex_md5(pass_1));
    }
    $.ajax({
        cache: false,
        type: "POST",
        url:"register",
        data:$('#regFor').serialize(),
        async: false,
        error: function(request) {
            alert("注册失败o(>﹏<)o了");
        },
        success: function(data) {
            var jsonObj = JSON.parse(data);
            if (jsonObj.Success){
                //申请成功， 跳转网页
                window.location.href="/";
            }else{
                //否则显示错误信息
                $("#regdata").html(jsonObj.html);
            }
        }
    });
}
