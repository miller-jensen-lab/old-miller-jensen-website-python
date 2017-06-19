import re
from google.appengine.ext import ndb
from wtforms import form
from wtforms.fields import (StringField, TextAreaField)
from wtforms.fields.html5 import DateField

class NewsItemForm(form.Form):
    title = StringField('Title')
    summary = TextAreaField('Summary')
    content = TextAreaField('Content')
    date_published = DateField('Date')

class NewsItem(ndb.Model):
    """ Model to store news about the lab.
    """
    title = ndb.StringProperty(indexed=False)
    summary = ndb.TextProperty(required=True)
    content = ndb.TextProperty(required=True)
    datetime_added = ndb.DateTimeProperty(auto_now_add=True)
    date_published = ndb.DateProperty(required=True)

    WS_RE = re.compile(r"\s+")

    @classmethod
    def nbsp(cls, x):
        """ Replace last space with an "&nbsp;"
        """
        y = cls.WS_RE.sub(' ', x.strip())
        y = "&nbsp;".join(y.rsplit(' ', 1))
        return y

    def get_as_markdown(self, summary=False, title_link=None):
        import logging
        logging.info('HERE I AM DUDE 1!!')

        # title = self.nbsp(self.title)
        title = self.title
        if title_link:
            retval = u'[{0}]({1}).'.format(title, title_link)
        else:
            retval = u'**{0}**.'.format(title)

        if summary:
            x = self.summary
        else:
            x = self.content
        retval = u"{0} {1}".format(retval, x)
        if not retval.endswith('.'):
            retval = u"{0}.".format(retval)

        retval = u"{0} _Posted&nbsp;{1}_".format(retval, self.date_published)
        logging.info(retval)
        return retval

    @classmethod
    def get_latest(cls, limit=10):
        return cls.query().order(-cls.date_published).fetch(limit=limit)
