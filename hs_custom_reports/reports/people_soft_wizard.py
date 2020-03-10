# -*- coding: utf-8 -*-


from odoo import models, fields, api, _

class PeopleSoftWizard(models.Model):
	_name = 'account.people.soft.wizard'
	_description = 'Final People Soft Wizzard'

	message = fields.Text(string="Advertencia", default="Esta apunto de "\
		"crear un reporte final de people soft. Una vez presione el boton "\
		"de aceptar, las facturas seleccionadas no estaran disponibles en "\
		"otros reportes finales de people soft.")


	def open_people_soft(self):
		return {
			'type': 'ir.actions.client',
			'name': _('People Soft'),
			'tag': 'people_soft',
			'options': {'partner_ids': [self.id]},
			'ignore_session': 'both',
			'context': "{'model':'account.peaplesoft.report'}"
		}