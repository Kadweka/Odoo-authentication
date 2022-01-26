from odoo import models, fields, api




class PartnerExtension(models.Model):
    _inherit = 'res.partner'

    password = fields.Text(string="partner password")
    f_name = fields.Char("First Name")
    l_name = fields.Char("Last Name")
    # clinic_name = fields.Char("Clinic Name")
    access_token_ids = fields.One2many(
        string='Access Tokens',
        comodel_name='jwt_provider.access_token',
        inverse_name='partner_id',
    )
