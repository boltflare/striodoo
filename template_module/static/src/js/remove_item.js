$( document ).ready(function() {
    $("#btn_search").click(function(){
        remover_item();
    });
    
 });
//document.getElementById("btn_search").onclick = remover_item;
function remover_item(){
    var list = document.getElementsByClassName("ui-sortable")[0];
    console.log(list);
    list.removeChild(list.childNodes[0]);
    console.log('Esta funcionando');
}