# -*- coding: utf-8 -*-
#############################################################################
#
#    Ingenuity Info
#
#    Copyright (C) 2023-TODAY Ingenuity Info(<https://ingenuityinfo.in>)
#    Author: Ingenuity Info(<https://ingenuityinfo.in>)
#
#
#############################################################################
{
    'name': "Sale Order Invoiced Grouped By Product",
    'author': "Ingenuity Info",
    'category': 'Accounting/Accounting',
    'summary': """ This Module will provide feature when invoicing a Sales Order or multiple at once, the invoice lines will be grouped based on product. """,
    'website': "https://ingenuityinfo.in",
    'company': 'Ingenuity Info',
    'maintainer': 'Ingenuity Info',
    'version': '15.0.0.0',
    'price': 0.0,
    'currency': 'EUR',
    'description': """ So if Sale Order SO001 contains Product-1 and Product-2, and Sale Order SO002 contains Product-1 and Product-3, the invoice generated when invoicing these two Sale Order at once will contain only 3 lines. System will combine the repeated Product in one single and sum it's Qty.  """,
    'depends': [
        'sale',
        'account',
    ],
    'data': [
    ],
    'qweb': [
        ],
    "assets": {
        "web.assets_backend": [
        ],
        "web.assets_tests": [
        ],
    },
    "images": ['static/description/Banner.gif'],
    "license": "AGPL-3",
    'installable': True,
    'application': True,
    'auto_install': False,
}