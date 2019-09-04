from odoo import models, fields, api, _
from odoo.exceptions import UserError
from pprint import pprint

class Sale(models.Model):
    _inherit = 'sale.order'

    employee_id = fields.Many2one('hr.employee', string='Salesman')

    @api.model
    def create(self, vals):
        res = super().create(vals)
        # if 'company_id' in vals:
        #     vals['name'] = self.env['ir.sequence'].with_context(
        #         force_company=vals['company_id']).next_by_code('sale.order') or _('New')
        # else:
        #     vals['name'] = self.env['ir.sequence'].next_by_code(
        #         'sale.order') or _('New')
        # update sequence name
        if res.employee_id.emp_code:
            print('Update Sale Order Number')
            res.write({
                'name' : 'SO/' + res.employee_id.emp_code + '/' + res.name 
            })
        return res
