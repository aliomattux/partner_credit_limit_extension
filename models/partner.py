from openerp.osv import osv, fields


class ResPartner(osv.osv):
    _inherit = 'res.partner'
    _columns = {
	'credit_history': fields.one2many('res.partner.credit.history', 'partner', 'Credit History', copy=False),
    }


class ResPartnerCreditHistory(osv.osv):
    _name = 'res.partner.credit.history'
    _columns = {
	'partner': fields.many2one('res.partner', 'Partner'),
	'adjustment_note': fields.char('Adjustment Note'),
	'previous_amount': fields.float('Previous Amount'),
	'new_amount': fields.float('New Amount'),
	'user': fields.many2one('res.users', 'User'),


    }
