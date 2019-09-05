from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProductUom(models.Model):
    _name = 'bja.product.uom'

    name = fields.Char(string='Name')
    