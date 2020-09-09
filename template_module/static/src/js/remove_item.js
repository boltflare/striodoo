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
    setTimeout(function(){ 
    console.log($("button[name*='search_visitor']"));
    $("button[name*='search_visitor']").attr("onclick","remover_item()");
     }, 2000);
      
      });
     });
    function remover_item(){
    setTimeout(function(){ 
    alert("termino");
     var list = document.getElementsByClassName("ui-sortable")[0];
        console.log(list);
        list.removeChild(list.childNodes[0]);
        console.log('Esta funcionando');
     }, 12000);
    }

