# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class Arrete(models.Model):#cette modele represente Arrete dans notre base de données
    _name = "gaff.arrete"
    _description = "Gestion des Arretée"
    _rec_name = "libelle"

    code = fields.char(string="CODE", required = True)
    date = fields.Date(string="DATE")