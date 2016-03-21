/**
 * Created by 香菇 on 2016/3/5.
 */
$(function(){
  if (window.location.pathname != "/"){
    window.location.href="/";
    return ;
  }
  $("#login_but").button();
  $("#login_but").click(function(){
    $.ajax({
        cache: false,
        type: "POST",
        url:"/",
        data:$('#login_form').serialize() + "&verInput=" + $("#verInput").val(),
        async: false,
        error: function(request) {
            alert('加载失败');
        },
        success: function(data) {
          var jsonObj = JSON.parse(data);

          if (jsonObj.Success){
            //申请成功， 跳转网页
            window.location.href="/Console";
          }else{
            //否则显示错误信息
            if (jsonObj.errID == 1){
              alert("用户名或密码错误");
            }
          }
        }
    });
  });
});


