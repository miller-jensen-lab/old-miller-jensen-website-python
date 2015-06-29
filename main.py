#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.appengine.users import admin_required

from models.publications import publications
from models.people import people
from models.newsitem import NewsItem, NewsItemForm
from google.appengine.api import users
import logging
import markdown2

class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        j2 = jinja2.get_jinja2(app=self.app)
        def md(*args, **kwargs):
            if args[0]:
                return markdown2.markdown(*args, **kwargs)
            return ''

        j2.environment.filters['markdown'] = md

        return j2

    def render_response(self, _template, **context):
        context = context or {}

        extra_context = {
          'request': self.request,
          'uri_for': self.uri_for,
        }

        # Only override extra context stuff if it's not set by the template:
        for key, value in extra_context.items():
            if key not in context:
                context[key] = value

        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)


class IndexPage(BaseHandler):
    def get(self):
        self.render_response(
            "index.html",
            tab='index',
            news_items=NewsItem.get_latest(limit=5)
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
        self.render_response(
            "news.html",
            tab="news",
            news_items=NewsItem.get_latest()
        )

class AdminPage(BaseHandler):
    def get(self):
        self.render_response(
            "admin/admin.html",
            tab="admin",
            news_items=NewsItem.get_latest()
        )


class NewsItemResource(BaseHandler):
    """
    NewsItemResource Reference

    There are 7 standard methods:
        index - GET /admin/news/
        show - GET /admin/news/{id}/
        edit - GET /admin/news/{id}/{action}/
        new - GET /admin/news/new/
        create - POST /admin/news/
        update - POST/PUT /admin/news/{id}/{action}/
        delete - POST/DELETE /admin/news/{id}/{action}/

    """

    INDEX_TEMPLATE = 'admin/news/list.html'
    DETAIL_TEMPLATE = 'admin/news/detail.html'

    def index(self):
        """
        Index method
        Display a list of new items

        """
        self.render_response(
            self.INDEX_TEMPLATE,
            news_items=NewsItem.get_latest(limit=1000)
        )

    def get(self):
        return self.index()

    def new(self):
        """
        New method

        Gather input to create a new news

        """
        form = NewsItemForm(self.request.POST)

        context = {
            'action': 'New',
            'form': form,
            'submit_routename': 'NewsItem.create'
        }

        self.render_response(self.DETAIL_TEMPLATE, **context)

    def create(self):
        """
        Create method

        Create a new news using posted data

        """
        # create form instance from the NewsItem
        form = NewsItemForm(self.request.POST)
        logging.info('Form = ')
        logging.info(form)

        context = {
            'action': 'New',
            'form': form,
            'submit_routename': 'NewsItem.create'
        }

        # since this method is only called from a post,
        # we do not need to check for request.method == "POST"
        # if self.form.validate() returns true, then save
        # the data
        if form.validate():
            logging.debug('Form Validated!')
            entity = NewsItem()
            # push form values into model
            form.populate_obj(entity)
            # save to data store
            key = entity.put()
            # redirect to index and/or edit form with new id
            logging.debug('key={0}'.format(key))
            # redirect to the edit page for the created id
            return webapp2.redirect_to('NewsItem.list', id=key.id())
        else:
            logging.warning('form failed to validate!')

        # the form did not validate, redisplay with errors
        return self.render_response(self.DETAIL_TEMPLATE, **context)

    def show(self, id):
        """
        Show method

        Show a specific news by id

        """
        context = {
            'action': 'Show',
            'id': id
         }

        self.render_response(self.DETAIL_TEMPLATE, **context)

    def edit(self, id):
        """
        Edit method

        Edit a specific news by id

        """
        entity_id = int(id)
        entity = NewsItem.get_by_id(entity_id)
        form = NewsItemForm(self.request.POST, obj=entity)

        context = {
            'action': 'Edit',
            'id': id,
            'form': form,
            'submit_routename': 'NewsItem.update'
         }

        self.render_response(self.DETAIL_TEMPLATE, **context)

    def update(self, id):
        """
        Update method

        Update an existing news by id
        Uses posted data from Edit method

        """
        # create form instance from the NewsItem
        entity_id = int(id)
        entity = NewsItem.get_by_id(entity_id)
        form = NewsItemForm(self.request.POST, obj=entity)

        context = {
            'id': id,
            'action': 'Update',
            'form': form,
            'submit_routename': 'NewsItem.update'
        }

        # since this method is only called from a post,
        # we do not need to check for request.method == "POST"
        # if self.form.validate() returns true, then save
        # the data
        if form.validate():
            logging.debug('Form Validated!')
            # push form values into model
            form.populate_obj(entity)
            # save to data store
            key = entity.put()
            # redirect to index and/or edit form with new id
            logging.debug('key={0}'.format(key))
            # redirect to the edit page for the created id
            return webapp2.redirect_to('NewsItem.list')

        # the form did not validate, redisplay with errors
        return self.render_response(self.DETAIL_TEMPLATE, **context)

    def delete(self, id):
        """
        New method

        Delete an existing news by id

        """
        context = {'action': 'Delete'}
        self.render_response(self.DETAIL_TEMPLATE, **context)



application = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=IndexPage),
    webapp2.Route(r'/people/', handler=PeoplePage),
    webapp2.Route(r'/publications/', handler=PublicationsPage),
    webapp2.Route(r'/news/', handler=NewsPage, name='news'),
    webapp2.Route(r'/admin/', handler=AdminPage),
    webapp2.Route(r'/admin/news/new/', handler=NewsItemResource, name='NewsItem.new', handler_method='new', methods='GET'),
    webapp2.Route(r'/admin/news/create/', handler=NewsItemResource, name='NewsItem.create', handler_method='create', methods='POST'),
    webapp2.Route(r'/admin/news/', handler=NewsItemResource, name='NewsItem.list', methods='GET'),
    webapp2.Route(r'/admin/news/<id:\d+>/', handler=NewsItemResource, name='NewsItem.edit', handler_method='edit', methods='GET'),
    webapp2.Route(r'/admin/news/<id:\d+>/update', handler=NewsItemResource, name='NewsItem.update', handler_method='update', methods='POST'),
    webapp2.Route(r'/admin/news/<id:\d+>/delete', handler=NewsItemResource, name='NewsItem.delete', handler_method='delete', methods='POST'),
], debug=True)
