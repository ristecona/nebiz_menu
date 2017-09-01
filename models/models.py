# -*- coding: utf-8 -*-

from odoo import models, fields, api

class nebiz_menu_item(models.Model):
    _name = 'nebiz.menu'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    