Title: Timestamps in Django
Date: 2008-09-03 19:00
Author: lindsayrgwatt
Category: Programming
Tags: django, Programming, python
Slug: timestamps-in-django
Status: published

I've recently been playing around with the [Django web framework](http://www.djangoproject.com/) (all non-techies should stop reading this at once).  Here's a little snippet of code that's useful if you want to add a timestamp to a model you're creating:

    from datetime import datetime

    class My_Model(models.Model):
      date_created = models.DateTimeField()
      date_modified = models.DateTimeField()

      def save(self):
        if self.date_created == None:
          self.date_created = datetime.now()
        self.date_modified = datetime.now()
        super(My_Model, self).save()

What happens is that when you save the object, you override the Django save method with your own. It checks to see if the object has a `date_created` timestamp. If it doesn't (i.e., you're creating it for the first time), it adds one. It also updates the `date_modified` timestamp every time you save it.

You might be wondering: why not just set the model to look like this:

    date_created = models.DateTimeField(default=datetime.now())

It won't work due to a quirk in Python. Python will calculate "`now`" to be the time when the model is loaded into interpreted. This means that every single object, until you restart the server, will get exactly the same timestamp. Not too useful - so use this hack instead.
