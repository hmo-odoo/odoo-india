# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class product_major_group(osv.Model):
    _name = 'product.major.group'
    _description = 'Product Major Group'

    _columns = {
        'name': fields.char('Name', size=256, required=True),
        'code': fields.char('Code', size=64, required=True),
    }

    _sql_constraints = [
        ('code_uniq', 'unique (code)', 'The code of the product major group must be unique!')
    ]

    def name_get(self, cr, uid, ids, context=None):
        res = []
        if not ids:
            return res
        # name_get may receive int id instead of an id list
        if isinstance(ids, (int, long)):
            ids = [ids]
        for major in self.browse(cr, uid, ids, context=context):
            name = "[%s] %s" % (major.code or '', major.name or '')
            res.append((major.id, name))
        return res

product_major_group()

class product_sub_group(osv.Model):
    _name = 'product.sub.group'
    _description = 'Product Major Group'

    _columns = {
        'name': fields.char('Name', size=256, required=True),
        'code': fields.char('Code', size=64, required=True),
        'major_group_id': fields.many2one('product.major.group', 'Major Group'),
    }

    _sql_constraints = [
        ('code_uniq', 'unique (code,major_group_id)', 'The code of the product sub group must be unique!')
    ]

    def name_get(self, cr, uid, ids, context=None):
        res = []
        if not ids:
            return res
        # name_get may receive int id instead of an id list
        if isinstance(ids, (int, long)):
            ids = [ids]
        for group in self.browse(cr, uid, ids, context=context):
            name = "[%s] %s" % (group.code or '', group.name or '')
            res.append((group.id, name))
        return res

product_sub_group()

class product_product(osv.Model):
    _inherit = 'product.product'
 
    _columns = {
        'major_group_id': fields.many2one('product.major.group', 'Major Group'),
        'sub_group_id': fields.many2one('product.sub.group', 'Sub Group'),
    }
 
product_product()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
