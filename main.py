#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webapp2
from models import publications, people
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


class IndexPage(BaseHandler):
    def get(self):
        self.render_response(
            "index.html",
            tab='index'
        )


class PeoplePage(BaseHandler):
    def get(self):
        self.render_response(
            "people.html",
            people=people,
            tab='people'
        )


class PublicationsPage(BaseHandler):
    def get(self):
        self.render_response(
            "publications.html",
            publications=publications,
            tab='publications'
        )

class NewsPage(BaseHandler):
    def get(self):
        self.render_response("news.html", tab="news")


application = webapp2.WSGIApplication([
    ('/', IndexPage),
    ('/people/', PeoplePage),
    ('/publications/', PublicationsPage),
    ('/news/', NewsPage),
], debug=True)
