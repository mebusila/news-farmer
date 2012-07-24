import webapp2
from models import *
import feedparser
import cgi
from time import mktime
from datetime import datetime
import hashlib

class UpdateHandler(webapp2.RequestHandler):
    def parseRss(self, feed):
        d = feedparser.parse(feed.feed_url)
        for entry in d.entries:
            m = hashlib.md5()
            m.update(cgi.escape(entry.description.encode('utf-8')))
            md5_hash = m.hexdigest()
            q = Item.gql(
                'WHERE link = :link AND published = :published',
                link = cgi.escape(entry.link),
                published = datetime.fromtimestamp(mktime(entry.updated_parsed))
            )
            item = q.get()
            if item == None:
                Item(
                    category = feed.category,
                    publisher = feed.publisher,
                    title = cgi.escape(entry.title),
                    link = cgi.escape(entry.link),
                    content = cgi.escape(entry.description),
                    content_md5 = md5_hash,
                    published = datetime.fromtimestamp(mktime(entry.published_parsed)),
                    updated = datetime.fromtimestamp(mktime(entry.updated_parsed))
                ).put()
            else:
                if item.content_md5 != md5_hash:
                    item.content = cgi.escape(entry.description)
                    item.content_md5 = md5_hash
                    item.updated = datetime.now()
                    item.put()

    def get(self):
        feeds = PublisherCategory.all()
        for feed in feeds:
            if feed.feed_type == "RSS":
                self.parseRss(feed)

app = webapp2.WSGIApplication([('/update', UpdateHandler)], debug=True)