# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_sale(models.Model):
    _inherit = "sale.order"

    x_slection = fields.Selection([
        ('1', 'HCOP'),
        ('2', 'FOH'),
        ('3', 'TAF505MC'),
        ('4', 'FSMK'),
    ], default='',
        string="材質", )
    x_slection2 = fields.Selection([
        ('1', '#25'),
        ('2', '#30'),
        ('3', '#40'),
    ], default='',
        string="厚み", )
    x_int = fields.Integer("巾")
    memo = fields.Text("メモ")
    x_slection3 = fields.Selection([
        ('1', '新規'),
        ('2', '変更'),
        ('3', ''),
    ], default='',
        string="内容", )
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     static = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
