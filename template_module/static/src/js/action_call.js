// alert("TEST1");
odoo.define('template_module.action_button', function (require) {
    "use strict";
    
    var rpc = require('web.rpc');
    var session = require('web.session');
    var _t = core._t;
    var core = require('web.core');
    // var ListView = require('web.ListView');
    var ListController = require("web.ListController");

    // alert("Va a llamar la funcion");
    ListController.include({
        renderButtons: function($node) {
        this._super.apply(this, arguments);
            if (this.$buttons) {
              this.$buttons.find('.oe_action_button').click(this.proxy('action_def'));
            }
        },

        action_def: function () {
            var self =this
            var user = session.uid;
            rpc.query({
                model: 'muki.rest',
                method: 'search_visitor',
                args: [[user],{'id':user}],
                }).then(function (e) {
                    self.do_action({
                        name: _t('wizard_form_search'),
                        type: 'ir.actions.act_window',
                        res_model: 'muki.rest',
                        views: [[false, 'form']],
                        view_mode: 'form',
                        target: 'new',
                    });
                    window.location
                });
            },
            

    // var IncludeListView = {
        
    //     renderButtons: function() {
    //         this._super.apply(this, arguments);
    //         // alert("TEST");
    //         if (this.modelName === "muki.rest") {
    //             var summary_apply_leave_btn = this.$buttons.find('button.oe_action_button');              
    //             summary_apply_leave_btn.on('click', this.proxy('oe_action_button'))
    //             // alert("ENTRO EN EL IF");
    //         }
    //     },
//         oe_action_button: function(){
//             var self = this;
//             var action = {
//                 type: "ir.actions.act_window",
//                 name: "Search Visitor",
//                 res_model: "muki.rest",
//                 // res_model: "visitor.wizard",
//                 views: [[false,'form']],
//                 target: 'new',
//                 // views: [[false, 'form']], 
//                 // view_type : 'form',
//                 view_mode : 'form',
//                 // view_id: 'view_visitor_wizard', 
//                 // flags: {'form': {'action_buttons': true, 'options': {'mode': 'edit'}}}
//             };
//             return this.do_action(action);
//         },
       
//     };
//     ListController.include(IncludeListView);
// });