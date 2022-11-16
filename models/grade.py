# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class Grade(models.Model):#Cette modele represente Grade dans notre base de données

    _name = "gaff.grade"
    _description = "Gestion des grades"
    _rec_name = "libelle"

    #fields veut dire champ
    code = fields.Char(string = "CODE", required = True)
    libelle = fields.Char(string = "LIBELLE")







# class SaleOrder(models.Model):
#     _name = "sale.order"
#     _description = "Sale Order"
#     _order = 'date_order desc, id desc'

#     name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, states={'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))
#     state = fields.Selection([
#         ('draft', 'Quotation'),
#         ('sent', 'Quotation Sent'),
#         ('sale', 'Sales Order'),
#         ('done', 'Locked'),
#         ('cancel', 'Cancelled'),
#         ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', track_sequence=3, default='draft')
#     date_order = fields.Datetime(string='Order Date', required=True, readonly=True, index=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]}, copy=False, default=fields.Datetime.now)
#     validity_date = fields.Date(string='Validity', readonly=True, copy=False, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
#         help="Validity date of the quotation, after this date, the customer won't be able to validate the quotation online.", default=_default_validity_date)
#     is_expired = fields.Boolean(compute='_compute_is_expired', string="Is expired")
#     remaining_validity_days = fields.Integer(compute='_compute_remaining_validity_days', string="Remaining Validity Days")
#     partner_shipping_id = fields.Many2one('res.partner', string='Delivery Address', readonly=True, required=True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)], 'sale': [('readonly', False)]}, help="Delivery address for current sales order.")