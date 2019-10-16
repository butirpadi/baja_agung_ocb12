from odoo import api, fields, models, _
from odoo.exceptions import UserError
from pprint import pprint


class BjaExpense(models.Model):
    _name = 'bja.expense'

    name = fields.Char(string='Name', required=True, default='New')
    expense_category_id = fields.Many2one(
        'expense.category', string='Expense Category', required=True)
    desc = fields.Char('Label', required=True)
    date = fields.Date('Date', required=True)
    partner_id = fields.Many2one('res.partner', string="Partner")
    amount = fields.Float(string="Amount", required=True, default=0.0)
    state = fields.Selection([('draft', 'Draft'), ('post', 'Post')],
                             string='State', required=True, default='draft')
    account_move_id = fields.Many2one('account.move', string='Journal Entries')

    def action_confirm(self):
        self.state = 'post'
        # posting to journal entry
        aml_dict = []
        print('Create Account Move Line')

        ref_name = self.desc

        # debit move
        aml_dict.append((0, 0, {
            'name': ref_name,
            'partner_id': self.partner_id.id,
            'debit': self.amount,
            'account_id': self.expense_category_id.account_id.id
        }))
        # credit move
        aml_dict.append((0, 0, {
            'name': ref_name,
            'partner_id': self.partner_id.id,
            'credit': self.amount,
            'account_id': self.expense_category_id.account_journal_id.default_debit_account_id.id
            
        }))
        print('done Create debit/credit account move line')

        acc_move = {
            'ref': self.name,
            'journal_id': self.expense_category_id.account_journal_id.id,
            'date': self.date,
            'line_ids': aml_dict
        }
        pprint(acc_move)
        self.account_move_id = self.env['account.move'].create(acc_move)
        self.account_move_id.post()

    def action_cancel(self):
        # cancel & delete journal entries
        self.state = 'draft'

    @api.multi
    def unlink(self):
        # Add code here
        if self.state == 'draft':
            return super(BjaExpense, self).unlink()
        else:
            raise UserError('You can not delete it on this state.')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(
                    force_company=vals['company_id']).next_by_code('bja.expense.seq') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'bja.expense.seq') or _('New')

        result = super(BjaExpense, self).create(vals)
        return result
