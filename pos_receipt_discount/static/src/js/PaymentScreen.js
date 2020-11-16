// window.onload = function() {
// 	document.getElementsByClassName("js_invoice").click();
// }
// odoo.define('pos_receipt_discount.PaymentScreen', function(require) {

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
/* console.log("Entro en el archivo")

$('document').ready(function(){
	$(".pay").click(function () {​​​​​
		hacerCheck();
		}​​​​​);
		$(".js_invoice").click(function () {​​​​​
		alert("The button was clicked.");
		}​​​​​);
		function hacerCheck() {​​​​​
		// $("#test").prop("checked", true);
		$(".js_invoice").trigger("click");
		}​​​​​
}); */


// });
/* odoo.define('pos_receipt_discount.PaymentScreen', function(require) {
	'use strict';
	console.log("Ento en el archivo")
	
	const PaymentScreen = require('point_of_sale.PaymentScreenWidget');
	const Registries = require('point_of_sale.Registries');


	const InvoiceButtonPaymentScreen = (PaymentScreen) =>
		class extends PaymentScreen {
		constructor() {
			super(...arguments);
			this.toggleIsToInvoice();
		}
	}

	Registries.Component.extend(PaymentScreen, InvoiceButtonPaymentScreen);
	return InvoiceButtonPaymentScreen;
}); */