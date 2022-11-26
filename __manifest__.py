# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'GESTION DES AFFECTATIONS',
    'version': '1.1',
    'category': 'Management',
    'summary': 'Gestion Des Affectations',
    'description': """
Cette application contient tout nos code source de gestions des affectations
    """,
    'sequence': 1,
    'depends': ['base'],
    'data': [
        # 'security/sale_security.xml',
        # 'security/ir.model.access.csv',
        # 'report/sale_report.xml',
        # 'report/sale_report_views.xml',
        # 'report/sale_report_templates.xml',
        # 'report/invoice_report_templates.xml',
        # 'report/report_all_channels_sales_views.xml',
        # 'data/ir_sequence_data.xml',
        # 'data/sale_data.xml',
        # 'data/mail_data.xml',
        # 'wizard/sale_make_invoice_advance_views.xml',
         'views/menu.xml',
         'views/grade_views.xml',
        'views/province_views.xml',
        'views/fonction_views.xml',
        'views/domaine_views.xml',
        'views/agent_views.xml',
        'views/appartenance_views.xml',
        'views/arrete_views.xml',
        'views/service_views.xml',
        'report/liste_agents.xml',
        'report/liste_arrete.xml'
        # 'views/mail_activity_views.xml',
        # 'views/assets.xml',
        # 'views/sale_portal_templates.xml',
        # 'views/sale_product_configurator_templates.xml',
        # 'views/sale_onboarding_views.xml',
        # 'views/res_config_settings_views.xml',
        # 'views/payment_views.xml',
        # 'views/product_attribute_views.xml',
        # 'wizard/sale_product_configurator_views.xml',
    ],
    'demo': [
        # 'data/sale_demo.xml',
        # 'data/product_product_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
