# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_master001(models.Model):
    _name = 'kki_master001.master'
    _description = 'kki_master001.master'

    name = fields.Char("登録者")
    code = fields.Char("商品コード")
    code2 = fields.Many2one("kki_master001.code2", string="得意先コード")
    description = fields.Char("銘柄")
    thickness = fields.Char("厚み")
    range = fields.Char("製品巾")
    range2 = fields.Char("原紙巾")
    classification = fields.Selection([
    ('1', '巻取'),
    ('2', '製袋'),
    ('3', 'その他'),
], default='',
    string="商品区分", )
    classification2 = fields.Selection([
    ('1', '丸投げ'),
    ('2', '加工依頼'),
    ('3', '材料'),
], default='',

    string="加工区分", )
    hinmei = fields.Text("品名")
    image = fields.Binary("画像")
    url = fields.Html("url")
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

