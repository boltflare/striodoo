// alert("TEST1");
odoo.define('template_module.action_call', function (require) {
    "use strict";

    var core = require('web.core');
    var ListView = require('web.ListView');
    var ListController = require("web.ListController");

    // alert("Va a llamar la funcion");
    var IncludeListView = {
        
        renderButtons: function() {
            this._super.apply(this, arguments);
            // alert("TEST");
            if (this.modelName === "muki.rest") {
                var summary_apply_leave_btn = this.$buttons.find('button.oe_action_button');              
                summary_apply_leave_btn.on('click', this.proxy('oe_action_button'))
                // alert("ENTRO EN EL IF");
            }
        },
        oe_action_button: function(){
            var self = this;
            var action = {
                type: "ir.actions.act_window",
                name: "Search Visitor",
                res_model: "visitor.wizard",
                views: [[false,'form']],
                target: 'new',
                views: [[false, 'form']], 
                view_type : 'form',
                view_mode : 'form',
                view_id: 'view_visitor_wizard', 
                // flags: {'form': {'action_buttons': true, 'options': {'mode': 'edit'}}}
            };
            return this.do_action(action);
        },

    };
    ListController.include(IncludeListView);
});