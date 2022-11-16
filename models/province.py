# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Province(models.Model):#Cette class represente notre model(objet) Province dans la base de données

    _name = "gaff.province"
    _description = "Gestion des provinces"
    _rec_name = "libelle"

    code = fields.Char(string = "CODE",required = True)
    libelle = fields.Char(string = "LIBELLE")