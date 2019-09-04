from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Users(models.Model):
    _inherit = 'res.users'

    notification_type = fields.Selection([
        ('email', 'Handle by Emails'),
        ('inbox', 'Handle in Apps')],
        'Notification Management', required=True, default='email',
        help="Policy on how to handle Chatter notifications:\n"
             "- Handle by Emails: notifications are sent to your email address\n"
             "- Handle in Apps: notifications appear in your Apps Inbox")

    