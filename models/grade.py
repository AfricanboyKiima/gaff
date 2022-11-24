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
