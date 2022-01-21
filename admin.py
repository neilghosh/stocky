from flask import Flask
from google.cloud import datastore
import binascii
import os
import logging


class KeysPage(webapp2.RequestHandler):
    def get(self):
        if '_method' in self.request.GET and self.request.GET['_method'] == 'delete':
            key = ndb.Key(urlsafe=self.request.GET['key'])
            logging.info("Deleting " + key.urlsafe() + " " + key.kind())
            key.delete()
            self.redirect("")
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hello, Admin!<hr>')
        qAll = ApiKey.query()
        apiKeys = qAll.fetch()
        self.response.out.write("<table border=1 cellpadding=10>")
        for apiKeyEntity in apiKeys:
            self.response.out.write(
                '<tr><td>'+apiKeyEntity.email + '</td><td>' + apiKeyEntity.api_key + '</td><td><a href="?_method=delete&key='+apiKeyEntity.key.urlsafe()+'">Delete</a></td></tr>')
        self.response.out.write("</table>")
        self.response.out.write(
            '<form method="post" >Email <input type="text" name="email"><input type="submit" name="add" value="Create New Key" ></form>')

    def post(self):
        newApiKey = binascii.hexlify(os.urandom(24))
        email = self.request.POST['email']
        keyEntity = ApiKey(email=email, api_key=newApiKey)
        keyEntity.put()
        self.redirect("")


app = webapp2.WSGIApplication([
    ('/admin/keys', KeysPage),
], debug=True)


class ApiKey(ndb.Model):
    email = ndb.StringProperty()
    api_key = ndb.StringProperty()
