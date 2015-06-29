from google.appengine.ext import ndb
from wtforms import form
from wtforms.fields import (StringField, TextAreaField)
from wtforms.fields.html5 import DateField

class NewsItemForm(form.Form):
    title = StringField('Title')
    content = TextAreaField('Content')
    date_published = DateField('Date')

class NewsItem(ndb.Model):
    """ Model to store news about the lab.
    """
    title = ndb.StringProperty(indexed=False)
    content = ndb.TextProperty(required=True)
    datetime_added = ndb.DateTimeProperty(auto_now_add=True)
    date_published = ndb.DateProperty(required=True)

    @classmethod
    def get_latest(cls, limit=10):
        return cls.query().order(-cls.date_published).fetch(limit=limit)
