# Copyright 2019-2025 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class ProductPricelistItem(models.Model):
    _inherit = "product.pricelist.item"
    # NOTE: we do not change _order, we are just adding sequence
    # and visualizing a different order in view.

    ppi_sequence = fields.Integer(default=16)
