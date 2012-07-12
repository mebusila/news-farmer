from google.appengine.ext import db

class Publisher(db.Model):
    name = db.StringProperty()
    def __unicode__(self):
        return self.name

class Category(db.Model):
    name = db.StringProperty()
    def __unicode__(self):
        return self.name

class PublisherCategory(db.Model):
    publisher = db.ReferenceProperty(Publisher)
    category = db.ReferenceProperty(Category)

    enabled = True
    feed_url = db.StringProperty()

class Item(db.Model):
    title = db.StringProperty()
    link = db.StringProperty()
    content = db.TextProperty()

    created = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now_add=True)

    publisher = db.ReferenceProperty(Publisher)
    category = db.ReferenceProperty(Category)

    def to_dict(self):
        return dict([(i, unicode(getattr(self, i))) for i in self.properties()])

    def __unicode__(self):
        return self.title