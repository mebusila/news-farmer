import webapp2
from models import *
import feedparser
import cgi
from time import mktime
from datetime import datetime

class UpdateHandler(webapp2.RequestHandler):
    def get(self):
        feeds = PublisherCategory.all()
        for feed in feeds:
            d = feedparser.parse(feed.feed_url)
            for entry in d.entries:
                q = Item.gql(
                    'WHERE link = :link AND published = :published',
                    link = cgi.escape(entry.link),
                    published = datetime.fromtimestamp(mktime(entry.updated_parsed))
                )
                if q.get() == None:
                    Item(
                        category = feed.category,
                        publisher = feed.publisher,
                        title = cgi.escape(entry.title),
                        link = cgi.escape(entry.link),
                        content = cgi.escape(entry.description),
                        published = datetime.fromtimestamp(mktime(entry.published_parsed)),
                        updated = datetime.fromtimestamp(mktime(entry.updated_parsed))
                    ).put()

app = webapp2.WSGIApplication([('/update', UpdateHandler)],
                              debug=True)