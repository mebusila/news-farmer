import webapp2

class UpdateHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(
            "asa"
        )

app = webapp2.WSGIApplication([('/update', UpdateHandler)],
                              debug=True)