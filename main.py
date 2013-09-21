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
                'postscript' : '(Research highlight in Nature Biotechnology, 9/07)',
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
