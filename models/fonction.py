# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class Fonction(models.Model):#Cette classe represente la table "fonction" dans notre base de donnée
    _name = "gaff.fonction"
    _description = "Gestion des fonctions"
    _rec_name = "libelle"



    code = fields.Char(string="CODE", required= True)
    libelle = fields.Char(string="LIBELLE")
    