import webapp2

class CategoriesHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('categories')

app = webapp2.WSGIApplication([('/categories', CategoriesHandler)],
    debug=True)
