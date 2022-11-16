# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class Service(models.Model):
    _name = "gaff.service"
    _description = "Gestion des services"
    _rec_name = "libelle"


    code = fields.Char(string="CODE",required=True)
    libelle = fields.Char(string="LIBELLE")