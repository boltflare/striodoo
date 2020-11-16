$('document').ready(function(){
 
    validar_boton_pay();
        
});

function hacerCheck() {
    $(".js_invoice").addClass("highlight");
    }

    function validar_boton_pay(){
        setTimeout(function(){
          var boton_pagar_cant=$(".pay").length;
          if(boton_pagar_cant<=0){
            validar_boton_pay();
          }
          else{
            $(".pay").click(function () {
                hacerCheck();
                });
                $(".js_invoice").click(function () {
                });
          }
        },1000)
      }
