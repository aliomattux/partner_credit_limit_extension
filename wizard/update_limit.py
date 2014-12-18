from openerp.osv import osv, fields


class PartnerCreditLimitWizard(osv.osv_memory):
    _name = 'partner.credit.limit.wizard'
    _columns = {
	'original_amount': fields.float('Original Amount'),
	'amount': fields.float('New Amount'),
	'adjustment_note': fields.char('Adjustment Note'),
    }


    def default_get(self, cr, uid, fields, context=None):
        if context is None: context = {}
        res = {}
	partner_obj = self.pool.get('res.partner')
        partner_ids = context.get('active_ids', [])
        partner = partner_obj.browse(cr, uid, partner_ids)[0]
	res.update({
		'original_amount': partner.credit_limit,
		'amount': partner.credit_limit,
	})

	return res


    def submit_change(self, cr, uid, ids, context=None):
	wizard = self.browse(cr, uid, ids[0])
	history_obj = self.pool.get('res.partner.credit.history')
	partner_obj = self.pool.get('res.partner')
        partner_ids = context.get('active_ids', [])
        partner = partner_obj.browse(cr, uid, partner_ids)[0]
	credit_limit = wizard.amount
	vals = {
		'partner': partner.id,
		'user': uid,
		'adjustment_note': wizard.adjustment_note or ' ',
		'previous_amount': wizard.original_amount,
		'new_amount': credit_limit,
	}

	partner_obj.write(cr, uid, partner.id, {'credit_limit': credit_limit})
	history_obj.create(cr, uid, vals)

	return True
