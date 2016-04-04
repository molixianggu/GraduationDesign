/**
 * Created by 香菇 on 2016/2/9.
 */
var debuging = true;
function debug_print(s){
    if (debuging){
        alert(s);
    }
}
function getLocalTime(nS) {
  return new Date(parseInt(nS) * 1000).toLocaleString().replace(/:\d{1,2}$/, ' ');
}
function _my_loadOver(name) {
  $(".ref").click(function () {
    if (my_exit_()) {
      getPage(name);
    }
  });
}
