# -*- coding: utf-8 -*-

from . import library
# from . import library2
import json
from odoo import models, fields, api


import logging
_logger = logging.getLogger(__name__)

class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    def action_muki_connect(self):
        # init API
        api = library.RestAPI()
        # api2 = library2.RestAPI()
        #api2.authenticate()
        api.authenticate()
        
        # test API
        logging.info(str(api.execute('/api')))
        logging.info(str(api.execute('/api/user')))

        #EJEMPLO FUNCIONAL 
        response = api.execute('/api/custom/create/vso')
        result = response['result']
        for entry in result:
            # estado = entry.get('hstatus')
            nombre = entry.get('name')
            correo = entry.get('email')
            visit = entry.get('visitor')
            self.env["muki.rest"].create({'visitor_name':nombre,'visitor_email':correo, 'visitor':visit})
            # self.env["res.partner"].create({'name':number,'hstatus':estado,'email':total,'visitor':visit})
            logging.info(str(response))

        # response = api.execute('/api/custom/create/vso')
        # result = response['result']
        # for entry in result:
        #     number = entry.get('name')
        #     total = entry.get('email')
        #     visit = entry.get('visitor')
        #     # self.env["muki.rest"].create({'name':number,'amount':total,'visita':visit})
        #     self.env["res.partner"].create({'name':number,'email':total,'visitor':visit})
        #     logging.info(str(response))

        #EJEMPLO NO FUNCIONAL
        """ response = api2.execute('/api/custom/create/vso')
        result = response['result']
        for entry in result:
            number = entry.get('name')
            total = entry.get('email')
            visit = entry.get('visitor')
        
        response = api2.execute('/api/custom/visitor/vso', type="POST")
        logging.info(str(response)) """
        

        # userinf = api.execute('/api/custom/hsusertype')
        #         result = userinf['result']
            
        #         logging.warning("result:" + str(result))
        #         for entry1 in result:
        #             usuarios = entry1.get('users')

    @api.multi
    def action_view_vso(self):
        vso_ids = self.id
        return{
            # 'name'          :   ('Project Cashflow Report'),
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'tree,form',
            # 'views': [(view_id_tree[0].id, 'tree'),(False,'form')],
            'target':'current', 
            'res_model':'muki.rest',
            'view_id ref="template_module.vso_tree_view"': '',
            'domain':[('project_id','in',[vso_ids])]
        }


    """ @api.multi
    def cmd_back(self,context=None):
        semester_ids=self.env['obe.core.semester'].search(
             [('department_id','=',context['department_id'])]).ids
        domain = [('id','in',semester_ids)]
        view_id_tree = self.env['ir.ui.view'].search(
             [('name','=',"semester.tree")])department_id=self.department_id.id)
        return {
         'type': 'ir.actions.act_window',
         # 'name': _('Product'),
         'res_model': 'obe.core.semester',
         'view_type': 'form',
         'view_mode': 'tree,form',
         'views': [(view_id_tree[0].id, 'tree'),(False,'form')],
         'view_id ref="obe_planning.semester_tree_view"': '',
         'target': 'current',
         'domain': domain,
        } """