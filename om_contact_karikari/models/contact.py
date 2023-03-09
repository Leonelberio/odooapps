from odoo import api, fields, models, _

class ContactInherited(models.Model):
    _inherit = 'res.partner'
    nom = fields.Char(String='Nom', required=True, tracking=True)
    prenoms = fields.Char(String='Prenoms', tracking=True)
    name = fields.Char(String='Nom complet', compute='_compute_full_name', store=True)
    source_acquisition = fields.Selection([('bouche_a_oreilles', 'Bouche à oreilles'), ('site_internet', 'Site Internet'), ('reseaux_sociaux', 'Réseaux sociaux'), ('boutique_salon_foire)', 'Boutique/Salon/Foire'), ('autres', 'Autres (Pécisez)')], String="Source d'acquisition", tracking=True)
    autre_source = fields.Char(String="Age", tracking=True)

    @api.depends('nom', 'prenoms')
    def _compute_full_name(self):
        for rec in self:
            rec.name = "%s %s" % (rec.prenoms, rec.nom)
            if rec.is_company:
                rec.prenoms = ''

    # is_child = fields.Boolean(String="Is child ?", tracking=True)
    # notes = fields.Text(String='Notes',tracking=True)
    # gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], String="Gender", tracking=True)
    #
    # # You can add readonly=False in the models or readonly=0 in XML(Views)
    # # If you want the compute field to be stored in the db, add store=True
    # capitalized_name = fields.Char(String='Capitalized name', compute='_compute_capitalized_name')
    #
    # @api.constrains('is_child', 'age')
    # def _check_child_age(self):
    #     for rec in self:
    #         if rec.is_child and rec.age == 0 :
    #             # _ is for translation purpose
    #             raise ValidationError(_('Age has to be recorded !'))
    #
    # @api.depends('name')
    # def _compute_capitalized_name(self):
    #     for rec in self:
    #         if rec.name:
    #             rec.capitalized_name = rec.name.upper()
    #         else:
    #             rec.capitalized_name = ''
    #
    # #API for onchange foction, You can add multiple fields
    # @api.onchange('source_acquisition')
    # def _onchange_age(self):
    #     if self.source_acquisition == 'autres':
    #         self.is_child = True
    #     else:
    #         self.is_child = False

