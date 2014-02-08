#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from config import config
import webapp2

from webapp2_extras import jinja2


class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)


class MainPage(BaseHandler):
    def get(self):
        papers = [
            {
                'title': u'Systems biology of virus-host signaling network interactions',
                'authors': 'Xue Q., Miller-Jensen K.',
                'year': 2012,
                'vol': 45,
                'issue': 4,
                'journal': "Trends in Biotechnology",
                'pmid': 22531130,
                'fulltext_url': 'http://www.bmbreports.org/fulltext/bmbreports/view.php?vol=45&page=213',
            },
            {
                'title': u'Varying virulence: epigenetic control of expression noise and disease processes',
                'authors': 'Miller-Jensen K., Dey S.S., Schaffer D.V., Arkin A.P.',
                'year': 2011,
                'vol': 29,
                'issue': 10,
                'journal': "Trends in Biotechnology",
                'pmid': 21700350,
                'fulltext_url': 'http://linkinghub.elsevier.com/retrieve/pii/S0167-7799(11)00093-X',
            },

            {
                'title': u'Genetic selection for context-dependent stochastic phenotypes: Sp1 and TATA mutations increase phenotypic noise in HIV-1 gene expression',
                'authors': 'Miller-Jensen K., Skupsky R., Shah P.S., Arkin A.P., Schaffer D.V.',
                'year': 2013,
                'vol': 9,
                'issue': 7,
                'journal': "PLoS Computational Biology",
                'pmid': 23874178,
                'fulltext_url': 'http://dx.plos.org/10.1371/journal.pcbi.1003135',
            },
            {
                'title': u'Chromatin accessibility at the HIV LTR promoter sets a threshold for NF-κB mediated viral gene expression',
                'authors': 'Miller-Jensen K., Dey S.S., Pham N., Foley J.E., Arkin A.P., Schaffer D.V.',
                'year': 2012,
                'vol': 4,
                'issue': 6,
                'journal': "Integrative Biology",
                'pmid': 22555315,
                'fulltext_url': 'http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3362694/',
            },
            {
                'title': 'Control of stochastic gene expression ' \
                    + 'by host factors at the HIV promoter',
                'authors': 'Burnett, J.C., Miller-Jensen, K., Shah, P.S.,' \
                    + 'Arkin, A.P., Schaffer, D.V.',
                'year': 2009,
                'vol': 5,
                'issue': 1,
                'journal': "PLoS Pathogens",
                'pmid': 19132086,
                'fulltext_url': 'http://www.plospathogens.org/article/' \
                    + 'info:doi/10.1371/journal.ppat.1000260',
            },
            {
                'title' : 'Common effector processing mediates cell-specific responses to stimuli',
                'authors' : 'Miller-Jensen, K.*, Janes, K.A.*, Brugge, J. S., Lauffenburger, D.A.',
                'year' : 2007,
                'journal' : "Nature" ,
                'pmid' : 17637676,
                'vol' : 448,
                'issue' : 7153,
                'pages' : '604-8',
                'fulltext_url' : 'http://www.nature.com/nature/journal/v448/n7153/abs/nature06001.html',
                'postscript' : '(Research highlight in Nature Biotechnology, 9/07)',
            },
            {
                'title' : 'Adenoviral vector saturates Akt pro-survival signaling and blocks insulin-mediated rescue of tumor necrosis-factor-induced apoptosis',
                'authors' : 'Miller-Jensen, K., Janes, K.A., Wong, Y., Griffith, L.G., Lauffenburger, D.A.',
                'year' : 2007,
                'journal' : "J Cell Science",
                'vol' : 119,
                'issue' : 18,
                'pages' : '3788-98',
                'pmid' : 16940353,
                'fulltext_url' : 'http://jcs.biologists.org/cgi/content/abstract/119/18/3788',
                'exports' : [
                    ('kyle', 'test')
                ]
            },
        ]
        self.render_response("index.html", papers=papers)


class JobsPage(BaseHandler):
    def get(self):
        self.render_response("jobs.html")

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/jobs/', JobsPage)
], debug=True)
