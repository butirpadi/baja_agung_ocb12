from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    bja_product_uom_id = fields.Many2one('bja.product.uom', string='Unit of Measure')

    