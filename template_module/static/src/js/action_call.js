console.log("rest");
odoo.define('template_module.action_call', function (require) {
    "use strict";

    var core = require('web.core');
    var ListView = require('web.ListView');
    var ListController = require("web.ListController");
    
    var rpc = require('web.rpc');
    var session = require('web.session');
    var _t = core._t;
    ListController.include({
       renderButtons: function($node) {
       this._super.apply(this, arguments);
           if (this.$buttons) {
             this.$buttons.find('.oe_action_button').click(this.proxy('search_visitor')) ;
           }
       },
        // var IncludeListView = {

        //     renderButtons: function() {
        //         this._super.apply(this, arguments);
        //         if (this.modelName === "muki.rest") {
        //             var summary_apply_leave_btn = this.$buttons.find('button.o_crete_leave_from_summary');              
        //             summary_apply_leave_btn.on('click', this.proxy('crete_leave_from_summary'))
        //         }
        //     },
        // receive_invoice: function () {
        //     var self = this
        //     var user = session.uid;
        //     rpc.query({
        //         model: 'muki.rest',
        //         method: 'action_muki_connect',
        //         args: [[user],{'id':user}],
        //         }).then(function (e) {
        //             self.do_action({
        //                 name: _t('action_invoices'),
        //                 type: 'ir.actions.act_window',
        //                 res_model: 'muki.rest',
        //                 views: [[false, 'form']],
        //                 view_mode: 'form',
        //                 target: 'new',
        //             });
        //             window.location
        //         });
        search_visitor: function(){
            var self = this;
            var action = {
                type: "ir.actions.act_window",
                name: "action_muki_connect",
                res_model: "muki.rest",
                views: [[false,'form']],
                target: 'new',
                views: [[false, 'form']], 
                view_type : 'form',
                view_mode : 'form',
                flags: {'form': {'action_buttons': true, 'options': {'mode': 'edit'}}}
            };
            return this.do_action(action);
        },

    });
    // ListController.include(IncludeListView);
});
