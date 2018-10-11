# -*- coding: utf-8 -*-

from odoo import models, fields, api

class  prestamo(models.Model):
	_name = 'prestamo.prestamo'
	nombre = 'fields.Char()'
	montoSolicitado = 'fields.Float()'
	interes = 'fields.Float()'
	meses = 'fields.Intenger()'
	montoapagar = 'fields.Float()'
# class prestamo(models.Model):
#     _name = 'prestamo.prestamo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
