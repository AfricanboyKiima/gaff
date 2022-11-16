# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class Domaine(models.Model):
    _name = "gaff.domaine"
    _description = "Gestion des domaine"
    _rec_name = "libelle" #this enables us enable naming of our tables on the user side


    code = fields.Char(string="CODE", required=True)
    libelle = fields.Char(string="LIBELLE")
    