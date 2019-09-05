from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.addons import decimal_precision as dp
from pprint import pprint

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    price_weight = fields.Float('Price/Weight', required=True, digits=dp.get_precision('Product Price'), default=0.0)
    product_weight = fields.Float(string='Weight', related='product_id.weight', store=True)
    bja_product_uom_id = fields.Many2one('bja.product.uom', related="product_id.bja_product_uom_id",string='UoM', store=True)

    @api.onchange('price_weight')
    def set_unit_price_on_price_weight_change(self):
        self.price_unit = self.product_weight * self.price_weight

    @api.model
    def create(self, vals):
        # set price_weight if nol
        prod = self.env['product.template'].search([('id','=',vals['product_id'])])
        if vals['price_weight'] == '' or vals['price_weight'] == 0:
            vals['price_weight']  = vals['price_unit'] / prod.weight
        res = super().create(vals)
        return res
    

    