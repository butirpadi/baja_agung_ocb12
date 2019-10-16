from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ExpenseCategory(models.Model):
    _name = 'expense.category'

    name = fields.Char(string='Name', required=True)
    account_id = fields.Many2one(
        'account.account', string='Expense Account', required=True)
    account_journal_id = fields.Many2one(
        'account.journal', string='Account Journal', required=True)
