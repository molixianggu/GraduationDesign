//
// Created by 香菇 on 2016/2/24.
//

$(function(){
  //离开事件
  $(window).bind('beforeunload',function(event){
    //return true;//'您输入的内容尚未保存，确定离开此页面吗？';
  });
  //昵称
  $("#loginBox span").text("你好," + $.cookie("nickName"));
  //侧边栏缩放
  $("#main_ico").click(function(){
    if ($("#leftBox").css("display") == "none"){
      $("#rightBox").animate({width: "80%"},"fast", function(){
        $("#leftBox").show("slow");
      });
    }else{
      $("#leftBox").hide("slow", function(){
        $("#rightBox").animate({width: "100%"},"fast");
      });
    }
  });
  //用户下拉窗
  $("#loginBox span").click(function(){
      $("#downBox").slideToggle("slow");
    });
  //关闭用户名显示
  $("#put_but").click(function(){
    if ($("#loginBox span").css("display") == "none"){
      $("#loginBox span").show("slow");
      $("#put_but").attr("src", "static/img/back_hover.png");
    }else{
      $("#downBox").hide("slow");
      $("#loginBox span").hide("slow");
      $("#put_but").attr("src", "static/img/back_hover2.png");
    }
  });
  //注册锁屏事件
  $("#bg-img").click(function(){
    $("#pass-Lock").slideToggle("slow");
    $("#pass-Lock").css("top", "40%").css("left", "60%");
    $("#pass-Lock input").focus();
  });
  $("#bg-img")[0].ondragstart = function(){return false;}
  $("#pass-Lock").on('keypress',function(event){
    if(event.keyCode == "13") {
      $("#pass-Lock").slideToggle("slow");
      $("#pass-Lock input").val("");
      $("#bg-img").fadeOut(1000);
      $.cookie("lock", 0);
    }
  });
  $("#bg-img").bind("contextmenu",function(e){
    return false;
  });
  $("#close").click(function(){
    //ajax
    window.location.href="/";
  });


  //右上角三个按钮
  $("#getHome").click(function(){
       if (my_exit_()){
         getPage("home");
       }
  });
  $("#Lock").click(function(){
    $.cookie("lock", 1);
    $("#bg-img").fadeIn(1000);
  });
  $("#cancellation").click(function(){
      if (my_exit_()){
        //删除cookie ， 跳转页面
        $.cookie("userName","");
        $.cookie("nickName","");
        $.cookie("levelName","");
        $.cookie("key","");
        window.location.href="/";
      }
  });
  //.............

  //加载锁屏
  if($.cookie("lock") == "1"){
    $("#bg-img").fadeIn(100);
  }
});


//$('body').oneTime('1das',function(){
////do something...
//});

//$(function(){
//    $("#menu").menu();
//    $.ajax({
//        cache: false,
//        type: "POST",
//        url:"http://127.0.0.1:8000",
//        data:"",
//        async: false,
//        error: function(request) {
//            debug_print('加载失败');
//        },
//        success: function(data) {
//            $("#loginBox").html(data);
//            //注册事件
//            $("#login").click(function(){
//                loginBox();
//            });
//            $("#register").click(function(){
//                registerBox();
//            });
//        }
//    });
//});
//
//function win_click_login(){
//    $("#ok").click(function(){
//        login();
//    });
//    $("#no").click(function(){
//        $(".window").hide("slow");
//    });
//    $(".window #messTitle img").click(function(){
//        $(this).parent().parent().hide("slow");
//    });
//}
//
//function win_click_register(){
//    $("#ok").click(function(){
//        register();
//    });
//    $("#no").click(function(){
//        $(".window").hide("slow");
//    });
//    $(".window #messTitle img").click(function(){
//        $(this).parent().parent().hide("slow");
//    });
//}
//
//function loginBox(){
//    $.ajax({
//        cache: false,
//        type: "POST",
//        url: "login",
//        data: "type=getForm",
//        async: false,
//        error: function (request) {
//            debug_print('加载失败');
//        },
//        success: function (data) {
//            $("#messBox").html(data);
//            $("#ok").button();
//            $("#no").button();
//            win_click_login();
//            popWindow();
//        }
//    });
//}
//function registerBox(){
//    $.ajax({
//        cache: false,
//        type: "POST",
//        url: "register",
//        data: "type=getForm",
//        async: false,
//        error: function (request) {
//            debug_print('加载失败');
//        },
//        success: function (data) {
//            $("#messBox").html(data);
//            $("#ok").button();
//            $("#no").button();
//            win_click_register();
//            popWindow();
//        }
//    });
//}
//
//
//function login(){
//    debug_print("hehe");
//}
//
//function register(){
//    var nickName = $("#id_nickName").val();
//    var userName = $("#id_loginName").val();
//    var pass_1 = $("#id_passWord").val();
//    var pass_2 = $("#id_repPassWord").val();
//    var invitation = $("#id_Invitation_code").val();
//    if (nickName == ""){
//        $("#register_error_1").html("<ul><li>请输入昵称</li></ul>");
//        return ;
//    }else{
//        $("#register_error_1").html("");
//    }
//    if (userName == ""){
//        $("#register_error_2").html("<ul><li>请输入用户名</li></ul>");
//        return ;
//    }else{
//        $("#register_error_2").html("");
//    }
//    if (pass_1 == ""){
//        $("#register_error_3").html("<ul><li>请输入登录密码</li></ul>");
//        if (pass_2 == ""){
//            $("#register_error_4").html("<ul><li>请再次输入密码</li></ul>");
//        }else{
//            $("#register_error_4").html("");
//        }
//        return ;
//    }else{
//        $("#register_error_3").html("");
//    }
//    if (pass_1.length < 6){$("#register_error_3").html("<ul><li>密码长度不能小于6位</li></ul>");return ;}
//    else{$("#register_error_3").html("");}
//    if (pass_1 != pass_2){
//        $("#register_error_4").html("<ul><li>两次输入不一致</li></ul>");
//        return ;
//    }else{
//        $("#register_error_4").html("");
//    }
//    if (invitation == ""){$("#register_error_5").html("<ul><li>请输入管理员提供的邀请码</li></ul>");return;}
//    else{$("#register_error_5").html("");}
//    $("#register_error_4").html("");
//    $("#id_passWord").val(hex_md5(pass_2));
//    $("#id_repPassWord").val(hex_md5(pass_1));
//    $.ajax({
//        cache: false,
//        type: "POST",
//        url:"register",
//        data:$('#registerForm').serialize() + "&type=sendForm",
//        async: false,
//        error: function(request) {
//            debug_print("注册失败o(>﹏<)o了");
//        },
//        success: function(data) {
//            var jsonObj = JSON.parse(data);
//            if (jsonObj.Success){
//                //申请成功， 跳转网页
//                window.location.href="/";
//            }else{
//                //否则显示错误信息
//                $("#messBox").html(jsonObj.html);
//                win_click_register();
//            }
//        }
//    });
//}
