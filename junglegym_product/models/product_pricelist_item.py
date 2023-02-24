# Copyright 2019-2022 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class ProductPricelistItem(models.Model):
    _inherit = "product.pricelist.item"
    # NOTE: we do not change _order, we ar jest adding sequence 
    # and visualizing a different order in view.

    ppi_sequence = fields.Integer(default=16)
