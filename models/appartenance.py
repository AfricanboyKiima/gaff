# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class Appartenance(models.Model):
    _name = "gaff.appartenance"
    _description = "Gestion des appartenance"
    _rec_name = "appartenance"


    agent = fields.Many2one("gaff.agent",string="AGENT")
    domaine = fields.Many2one("gaff.domaine",string="DOMAINE")

