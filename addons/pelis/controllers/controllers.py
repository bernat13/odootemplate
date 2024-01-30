# -*- coding: utf-8 -*-
from odoo import http

class Pelis(http.Controller):
    @http.route('/pelis/pelis/', auth='public')
    def index(self, **kw):
        return "<h1>Hola modulo de pelis</h1>"

    @http.route('/pelis/pelis/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('pelis.listing', {
            'root': '/pelis/pelis',
            'objects': http.request.env['pelis.pelis'].search([]),
        })

    @http.route('/pelis/pelis/objects/<model("pelis.pelis"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('pelis.object', {
            'object': obj
        })

