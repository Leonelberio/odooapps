from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = 'mail.thread'
    _description = "Patient Record"

    name = fields.Char(String='Name', required=True, tracking=True)
    age = fields.Integer(String="Age", tracking=True)
    is_child = fields.Boolean(String="Is child ?", tracking=True)
    notes = fields.Text(String='Notes',tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], String="Gender", tracking=True)

    # You can add readonly=False in the models or readonly=0 in XML(Views)
    # If you want the compute field to be stored in the db, add store=True
    capitalized_name = fields.Char(String='Capitalized name', compute='_compute_capitalized_name')

    @api.constrains('is_child', 'age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0 :
                # _ is for translation purpose
                raise ValidationError(_('Age has to be recorded !'))

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''

    #API for onchange foction, You can add multiple fields
    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False

