import webapp2
from models import *
import json

class PublishersHandler(webapp2.RequestHandler):
    def get(self):
        try:
            limit = int(self.request.get('limit'))
        except :
            limit = 10000

        items = PublisherCategory.all().fetch(limit)
        publishers = []
        for item in items:
            add = True
            for publisher in publishers:
                if publisher.key() == item.publisher.key():
                    add = False
                    break

            if(add):
                publishers.append(
                    item.publisher
                )

        self.response.write(
            json.dumps(
                [publisher.to_dict() for publisher in publishers]
            )
        )

app = webapp2.WSGIApplication([('/publishers', PublishersHandler)],
    debug=True)
