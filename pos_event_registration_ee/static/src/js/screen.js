odoo.define('pos_event_registration_ee.screen', function (require) {
"use strict";

var core = require('web.core');
var utils = require('web.utils');
var rpc = require('web.rpc');
var screens = require('point_of_sale.screens');
var gui = require('point_of_sale.gui');
var models = require('point_of_sale.models');
var PopupWidget = require('point_of_sale.popups');
var PosBaseWidget = require('point_of_sale.BaseWidget');
var field_utils = require('web.field_utils');

var QWeb = core.qweb;
var _t = core._t;

    models.load_models({
        model:  'event.event',
        fields: [],
        domain: null,
        loaded: function(self, events){
            self.events = events;
        }
    });
    models.load_models({
        model:  'pos.event.ticket',
        fields: [],
        domain: null,
        loaded: function(self, event_tickets){
            self.event_tickets = event_tickets;
        }
    });

	var EventRegistrationPopup = PopupWidget.extend({
	    template: 'EventRegistrationPopup',

	    init: function(parent, args) {
	    	var self = this;
	        this._super(parent, args);
	    },
	    show: function(options){
            var self = this;
            this._super(options);
            this.events = options.events || false;
            this.$('.event-list-contents').delegate('.event-line','click',function(event){
                self.line_select(event,$(this),parseInt($(this).data('id')));
            });
            this.renderElement();
        },
        events:{
	      'click .today':'click_today',
	      'click .another_day' : 'click_another_day',
	      'click .confirm' : 'click_confirm',
	      'click .cancel' : 'click_cancel',
	    },
        renderElement : function(){
	        var self = this;
	        this._super();
            if(this.pos.get_order().get_selected_orderline()){
	            self.render_list_today(this.pos.event_tickets);
	        }

	        $('.cancel').on('click',function(){
                self.gui.close_popup();
	        });

	        $('.another_day').on('click',function(){
                self.click_another_day();
	        });

	        $('.today').on('click',function(){
                self.click_today();
	        });

	        $('.confirm').on('click',function(){
                self.click_confirm();
	        });

	        this.$('.event-list-contents').delegate('.event-line','click',function(event){
                self.line_select(event,$(this),parseInt($(this).data('id')));
            });
	    },

	    render_list_today: function(event_tickets){
            var contents = this.$el[0].querySelector('.event-list-contents');
            contents.innerHTML = "";
            this.$('.today').addClass('highlightb');
            this.$('.another_day').removeClass('highlightb');
            var list = event_tickets;
            var f_list = _.pluck(list, 'event_id');
            var events = this.events;
            var date_list = []
            for(var i = 0, len = Math.min(events.length,1000); i < len; i++){
                var date_begin = moment(moment(events[i].date_begin).format('L'));
                var date_end = moment(moment(events[i].date_end).format('L'));
                var today = moment(moment().format('MM/DD/YYYY'))
                if( (date_begin.isSame(today)) || (date_end.isSame(today)) || (date_begin.isBefore(today) && !date_end.isBefore(today))){
                    date_list.push(events[i].id);
                }
            }
            var p_id = this.pos.get_order().get_selected_orderline().product.id;
            for(var i = 0, len = Math.min(event_tickets.length,1000); i < len; i++){
                if(event_tickets[i].product_id[0] == p_id && date_list.includes(event_tickets[i].event_id[0])){
                    var event_ticket    = event_tickets[i];
                    var eventline_html = QWeb.render('EventLine',{widget: this, event_ticket:event_tickets[i]});
                    var eventline = document.createElement('tbody');
                    eventline.innerHTML = eventline_html;
                    eventline = eventline.childNodes[1];
                    contents.appendChild(eventline);
                }
            }
        },

        render_list_another: function(event_tickets){
            var contents = this.$el[0].querySelector('.event-list-contents');
            contents.innerHTML = "";
            var list = event_tickets;
            var f_list = _.pluck(list, 'event_id');
            var events = this.events;
            var date_list = []
            for(var i = 0, len = Math.min(events.length,1000); i < len; i++){
                var date_begin = moment(moment(events[i].date_begin).format('L'));
                var date_end = moment(moment(events[i].date_end).format('L'));
                var today = moment(moment().format('MM/DD/YYYY'))
                if(!(date_end.isBefore(today)) && !(date_begin.isSame(today))){
                    date_list.push(events[i].id);
                }

            }
            var p_id = this.pos.get_order().get_selected_orderline().product.id;
            for(var i = 0, len = Math.min(event_tickets.length,1000); i < len; i++){
                if(event_tickets[i].product_id[0] == p_id && date_list.includes(event_tickets[i].event_id[0])){
                    var event_ticket    = event_tickets[i];
                    var eventline_html = QWeb.render('EventLine',{widget: this, event_ticket:event_tickets[i]});
                    var eventline = document.createElement('tbody');
                    eventline.innerHTML = eventline_html;
                    eventline = eventline.childNodes[1];
                    contents.appendChild(eventline);
                }
            }
        },

        line_select: function(event,$line,id){
            this.$('.event-list .lowlighte').removeClass('lowlighte');
            if ( $line.hasClass('highlighte') ){
                $line.removeClass('highlighte');
                $line.addClass('lowlighte');
            }else{
                this.$('.event-list .highlighte').removeClass('highlighte');
                $line.addClass('highlighte');
            }
        },

        click_today:function(){
	       var self = this;
	       self.render_list_today(this.pos.event_tickets);
	    },
	    click_another_day:function(){
	        var self = this;
            this.$('.today').removeClass('highlightb');
            this.$('.another_day').addClass('highlightb');
            self.render_list_another(this.pos.event_tickets);

	    },

	    click_confirm: function(){
                var self = this;
                var line = this.pos.get_order().get_selected_orderline();
                if(document.getElementsByClassName('highlighte').length != 0){
                    var event = document.getElementsByClassName('highlighte')[0].innerText;
                    var id = Number($(".highlighte")[0].getAttribute('data-id'));
                    var ticket_id = Number($(".highlighte")[0].getAttribute('data-ticket_id'));
                    line.set_id(id);
                    line.set_event(event);
                    line.set_ticket_id(ticket_id)
                    self.gui.close_popup();
                }
	    },
	    click_cancel:function(){
	        var self = this;
	        self.gui.close_popup();
	    },

	});
	gui.define_popup({name:'EventRegistrationPopup', widget: EventRegistrationPopup});

	var EventRegistrationButton = screens.ActionButtonWidget.extend({
        template: 'EventRegistrationButton',
        button_click: function(){
            var self = this;
            var events = self.pos.events
            var line = this.pos.get_order().get_selected_orderline();
            if (line) {
                this.gui.show_popup('EventRegistrationPopup',{events:events});
            }
        },
    });

    screens.define_action_button({
        'name': 'event_registration',
        'widget': EventRegistrationButton,
    });

    var _super_orderline = models.Orderline.prototype;

    models.Orderline = models.Orderline.extend({
        initialize: function(attr, options) {
            _super_orderline.initialize.call(this,attr,options);
            this.event = this.event || "";
            this.event_id = this.event || false;
            this.event_ticket_id = this.event || false;

        },
        set_event: function(event){
            this.event = event;
//            this.trigger('change',this);
        },
        get_event: function(event){
            return this.event;
        },
        set_ticket_id: function(event_ticket_id){
            this.event_ticket_id = event_ticket_id;
//            this.trigger('change',this);
        },
        get_ticket_id: function(ticket_id){
            return this.event_ticket_id;
        },
        set_id: function(id){
            this.event_id = id;
//            this.trigger('change',this);
        },
        get_id: function(event){
            return this.event_id;
        },
        export_as_JSON: function(){
            var json = _super_orderline.export_as_JSON.call(this);
            json.event = this.get_event();
            json.event_id = this.get_id();
            json.event_ticket_id = this.get_ticket_id();
            return json;
        },
        init_from_JSON: function(json){
            _super_orderline.init_from_JSON.apply(this,arguments);
            this.event = json.event;
            this.event_id = json.event_id;
            this.event_ticket_id = json.event_ticket_id;
        },
    });
});