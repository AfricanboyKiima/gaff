# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class Agent(models.Model):# class est une representation instructif d'un objet
    _name = "gaff.agent"
    _description = "Gestion des agents"
    _rec_name = "nom"

    matricule = fields.Char(string="MATRICULE",required=True)
    nom = fields.Char(string="NOM")
    postnom = fields.Char(string="POSTNOM")
    prenom = fields.Char(string="PRENOM")
    datenaissance = fields.Char(string="DATENAISSANCE")
    lieunaissance = fields.Char(string="LIEUNAISSANCE")
    sexe = fields.Char(string="SEXE")
    tel = fields.Char("TELEPHONE")
    adresse = fields.Text("ADRESSE")
    fonction = fields.Many2one("gaff.fonction", string="FONCTION")
    grade = fields.Many2one("gaff.grade", string="GRADE")
    arrete = fields.Many2one("gaff.arrete", string="ARRETE")
    province = fields.Many2one("gaff.province",string="PROVINCE")
    service = fields.Many2one("gaff.service",string="SERVICE")