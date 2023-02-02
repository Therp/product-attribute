# Copyright 2019-2022 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import _, api, fields, models, exceptions


class ProductPricelistItem(models.Model):
    _inherit = "product.pricelist.item"
    _order = "sequence, applied_on, min_quantity desc, categ_id desc, id desc"
    # NOTE: if you change _order on this model, make sure it matches the SQL
    # query built in _compute_price_rule() above in this file to avoid
    # inconstencies and undeterministic issues.

    sequence = fields.Integer(default=16)

