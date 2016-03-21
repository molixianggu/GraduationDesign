/**
 * Created by 香菇 on 2016/2/27.
 */

var windowHeight;
var windowWidth;
var popWidth;
var popHeight;

function init(){
    windowHeight=$(window).height();
    windowWidth=$(window).width();
    popHeight=$(".window").height();
    popWidth=$(".window").width();
}
function closeWindow(){
    $(".window #messTitle img").click(function(){
        $(this).parent().parent().hide("slow");
    });
}
function popWindow(){
    init();
    //使弹窗居中
    var popY=(windowHeight-popHeight)/2;
    var popX=(windowWidth-popWidth)/2;
    $(".window").css("top",popY).css("left",popX).slideToggle("slow");
    closeWindow();//关闭事件
}

