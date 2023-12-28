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
from itertools import groupby
from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError, ValidationError

import logging
_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'sale.order'

    
    def action_post(self):
        res = super(AccountMove, self).action_post()
        line_ids = self.mapped('line_ids').filtered(lambda line: line.sale_line_ids.is_downpayment)
        for line in line_ids:
            try:
                line.sale_line_ids.tax_id = line.tax_ids
                if all(line.tax_ids.mapped('price_include')):
                    line.sale_line_ids.price_unit = line.price_unit
                else:
                    line.sale_line_ids.price_unit = -line.sale_line_ids.untaxed_amount_to_invoice
            except UserError:
                pass
        return res
