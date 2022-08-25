# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_purchase(models.Model):
    _inherit = "purchase.order"

    memo = fields.Text("メモ")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     static = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
