// $( document ).ready(function() {
//     alert("TEST1");
//     $(".oe_highlight").click(function(){
//         remover_item();
//     });
    
//  });
// //document.getElementById("btn_search").onclick = remover_item;
// function remover_item(){
//     var list = document.getElementsByClassName("ui-sortable")[0];
//     console.log(list);
//     list.removeChild(list.childNodes[0]);
//     console.log('Esta funcionando');
// }
$( document ).ready(function() {
    
    $(".oe_action_button").click(function(){
        remover_item();
    });
    
 });
//document.getElementById("btn_search").onclick = remover_item;
function remover_item(){
setTimeout(function(){ 

var list = document.getElementsByClassName("ui-sortable")[0];
    console.log(list);
    list.removeChild(list.childNodes[0]);
    console.log('Esta funcionando');
}, 10000);
   
}

