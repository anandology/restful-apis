"""Blog API v1.

Simple RESTful API for a blog engine with posts.

See api.txt for more details.
"""
import web
from . import db
from .utils import json_response, jsondata

urls = (
    "/", "index",
    "/posts",  "posts",
    "/posts/(\d+)", "post",
)
app = web.application(urls, globals())

class index:
    def GET(self):
        response = {"service": "Blog API", "version": 1}
        return json_response(response)

class posts:
    def GET(self):
        """Get all posts.
        """
        posts = db.get_posts()
        return json_response(posts)

    def POST(self):
        """Create a new post.
        """
        data = jsondata()
        # TODO: do validation
        post = db.create_post(data['title'], data['body'])
        return json_response(post)

class post:
    def GET(self, id):
        """Read a post.
        """
        post = self.get_post(id)
        return json_response(post)

    def PUT(self, id):
        """Update a post.
        """
        post = self.get_post(id)
        data = jsondata()
        # TODO: do validation
        db.update_post(post.id, data['title'], data['body'])
        return db.get_post(id)

    def DELETE(self, id):
        """Deletes a post.
        """
        # this is 404 if post is not found
        post = self.get_post(id)

        db.delete_post(post.id)
        return json_response({})

    def get_post(self, id):
        post = db.get_post(id)
        if not post:
            raise web.notfound()
        return post
