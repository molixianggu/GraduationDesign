/**
 * Created by 香菇 on 2016/3/5.
 */
function getPage(s){
  $.ajax({
    cache: false,
    type: "POST",
    url:"getPage",
    data:"getType=" + s + ".html",
    async: false,
    error: function(request) {
      alert('加载失败');
    },
    success: function(data) {
      $("#rightBox").html(data);

    }
  });
}
function my_exit_(){

}
$(function(){
  //添加父li标签展开事件
  $(".par").click(function(){
    var li_obj = $(".par");
    for (var i = 0 ; i < li_obj.length ; i ++){
      if (this != li_obj[i]){
        $(li_obj[i]).find("li").hide("slow");
      }else{
        $(this).find("li").slideToggle("slow");
      }
    }
  });

  //添加子菜单事件
  var li_tab = $(".sub_meun").find("li");
  for (var i = 0 ; i < li_tab.length ; i ++){
    $(li_tab[i]).click(function(){
      var li_id = $(this).attr("id");
      if (li_id != undefined){
        if (my_exit_()){
          getPage(li_id);
        }
      }
      return false;
    });
  }

  //加载主页
  getPage("home");

});
