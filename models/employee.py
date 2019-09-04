from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Employee(models.Model):
    _inherit = 'hr.employee'

    emp_code = fields.Char('Employee Code', required=True)

    