from google.appengine.ext import db

class Publisher(db.Model):
    name = db.StringProperty()

    def __unicode__(self):
        return self.name

    def to_dict(self):
        return dict([(i, unicode(getattr(self, i))) for i in self.properties()])

class Category(db.Model):
    name = db.StringProperty()

    def __unicode__(self):
        return self.name

    def to_dict(self):
        return dict([(i, unicode(getattr(self, i))) for i in self.properties()])

class PublisherCategory(db.Model):
    publisher = db.ReferenceProperty(Publisher)
    category  = db.ReferenceProperty(Category)

    enabled   = True
    feed_url  = db.StringProperty()
    feed_type = db.StringProperty(choices=set(["RSS", "ATOM"]), default="RSS")

class Item(db.Model):
    title       = db.StringProperty()
    link        = db.StringProperty()
    content     = db.TextProperty()
    content_md5 = db.StringProperty()

    published   = db.DateTimeProperty()
    updated     = db.DateTimeProperty()

    created     = db.DateTimeProperty(auto_now_add=True)

    publisher   = db.ReferenceProperty(Publisher)
    category    = db.ReferenceProperty(Category)

    def to_dict(self):
        return dict([(i, unicode(getattr(self, i))) for i in self.properties()])

    def __unicode__(self):
        return self.title