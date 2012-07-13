import webapp2
from models import *
import feedparser
import cgi

class UpdateHandler(webapp2.RequestHandler):
    def get(self):
        feeds = PublisherCategory.all()
        for feed in feeds:
            d = feedparser.parse(feed.feed_url)
            for entry in d.entries[:15]:
                Item(
                    category = feed.category,
                    publisher = feed.publisher,
                    title = cgi.escape(entry.title),
                    link = cgi.escape(entry.link),
                    content = cgi.escape(entry.description)
                ).put()

app = webapp2.WSGIApplication([('/update', UpdateHandler)],
                              debug=True)