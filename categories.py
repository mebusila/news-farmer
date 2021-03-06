import webapp2
from models import *
import json

class CategoriesHandler(webapp2.RequestHandler):
    def get(self):
        try:
            limit = int(self.request.get('limit'))
        except :
            limit = 10000

        items = PublisherCategory.all().fetch(limit)
        categories = []
        for item in items:
            add = True
            for category in categories:
                if category.key() == item.category.key():
                    add = False
                    break

            if(add):
                categories.append(
                    item.category
                )

        self.response.write(
            json.dumps(
                [category.to_dict() for category in categories]
            )
        )

app = webapp2.WSGIApplication([('/categories', CategoriesHandler)],
    debug=True)
