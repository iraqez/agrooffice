# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Delice (<http://proyectodelice.es>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
from osv import osv, fields
from tools.translate import _

class agro_project_cultivo(osv.osv):    
    _name = 'agro.project.cultivo'
    _description = 'Tipo de cultivo'
    
    _columns={
            'name': fields.char('Cultivo', size=128, required = True),
              }
    
agro_project_cultivo()

class agro_project_variedad(osv.osv):
    _name = 'agro.project.variedad'
    _description = 'Variedad de cultivo'

    _columns={
            'name': fields.char('Variedad', size=128, required = True),
            'cultivo_id': fields.many2one('agro.project.cultivo', 'Cultivo', required = True),
              }

agro_project_variedad()

class agro_project_explotacion(osv.osv):
    _name = 'agro.project.explotacion'
    _description = 'Explotacion'

    _columns={
            'name': fields.char('Nombre', size=60, required = True),
            'propietario_id': fields.many2one('res.partner', 'Propietario', required=True),
            'ref_catastral': fields.char('Ref. Catastral', size=30),
            'prop_tomo': fields.integer('Tomo'),
            'prop_libro': fields.integer('Libro'),
            'prop_folio': fields.integer('Folio'),
            'prop_inscripcion': fields.integer('Inscripcion'),
            'prop_fecha': fields.date('Fecha inscripcion'),
            'sigpac_prov': fields.integer('Provincia'),
            'sigpac_muni': fields.integer('Municipio'),
            'sigpac_pol': fields.integer('Poligono'),
            'sigpac_par': fields.integer('Parcela'),
            'sigpac_rec': fields.integer('Recinto'),
            'superficie': fields.float('Superficie (Ha)'),
            'riego': fields.boolean('Tiene riego'),
            'tipo_riego': fields.char('Tipo de riego', size=128),
            'variedad_id': fields.many2one('agro.project.variedad', 'Variedad', size=128, required = True),
            'cultivo_id': fields.many2one('agro.project.cultivo', 'Cultivo', required = True),
            'num_plantas': fields.integer('Num. plantas'),
            'campana_ids': fields.one2many('project.project', 'explotacion_id', 'Campanas'),
              }

agro_project_explotacion()

class agro_res_partner_explotacion(osv.osv):
    _inherit = 'res.partner'

    _columns={
            'explotacion_ids': fields.one2many('agro.project.explotacion', 'propietario_id', 'Explotaciones'),
    }

agro_res_partner_explotacion()
