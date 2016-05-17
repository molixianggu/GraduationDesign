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
  $("#bg-imgs").click(function () {
    $("#pass-Lock").slideToggle("slow");
    $("#pass-Lock").css("top", "40%").css("left", "60%");
    $("#pass-Lock input").focus();
  });
  $("#bg-imgs")[0].ondragstart = function () {
    return false;
  }
  $("#pass-Lock").on('keypress',function(event){
    if(event.keyCode == "13") {
      $("#pass-Lock").slideToggle("slow");

      if ($.cookie("pw") == $("#pass-Lock input").val()){
        $("#pass-Lock input").val("");
        $("#bg-imgs").fadeOut(1000);
        $.cookie("lock", 0);
      }else{
        alert("密码错啦");
      }

    }
  });
  $("#bg-imgs").bind("contextmenu", function (e) {
    return false;
  });
  $("#close").click(function(){
    //删除cookie ， 跳转页面
    if (my_exit_()) {
      $.cookie("userName", "");
      $.cookie("nickName", "");
      $.cookie("levelName", "");
      $.cookie("key", "");
      $.cookie("lock", "");
      window.location.href = "/";
    }
  });


  //右上角三个按钮
  $("#getHome").click(function(){
       if (my_exit_()){
         getPage("home");
       }
  });
  $("#Lock").click(function(){
    var pw = $.cookie("pw");
    if (pw == undefined){
      pw = prompt("请设置锁屏密码");
      if (pw != ""){
        $.cookie("pw", pw);
        $.cookie("lock", 1);
        $("#bg-imgs").fadeIn(1000);
      }
    }
    $.cookie("lock", 1);
    $("#bg-imgs").fadeIn(1000);
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
    $("#bg-imgs").fadeIn(100);
  }
});
