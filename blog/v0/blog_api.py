import web
import json
import db

urls = (
    "/", "index",
    "/list-posts",  "posts",
    "/create-post", "create",
    "/update-post", "update",
    "/show-post", "show",
    "/delete-post", "delete",
)
app = web.application(urls, globals())

def json_response(data):
    web.header("Content-Type", "application/json")
    return json.dumps(data)

def jsondata():
    payload = web.data().decode("utf-8")
    return json.loads(payload)

class index:
    def GET(self):
        response = {"service": "Blog API", "version": 0}
        return json_response(response)

class posts:
    def GET(self):
        posts = db.get_posts()
        return json_response(posts)

class create:
    def POST(self):
        payload = jsondata()
        data = payload["post"]
        # TODO: validate data
        post_id = db.create_post(data['title'], data['body'])
        response = {"status": "created", "id": post_id}
        return json_response(response)

class update:
    def POST(self):
        i = web.input(id=None)
        if not i.id:
            return json_response({"error": "id not provided"})

        post = db.get_post(i.id)
        if not post:
            return json_response({"error": "post not found"})

        payload = jsondata()
        data = payload["post"]
        # TODO: validate data
        db.update_post(i.id, data['title'], data['body'])
        response = {"status": "updated"}
        return json_response(response)

class show:
    def GET(self):
        i = web.input(id=None)
        if not i.id:
            return json_response({"error": "id not provided"})

        post = db.get_post(i.id)
        if not post:
            return json_response({"error": "post not found"})

        return json_response(post)

class delete:
    def GET(self):
        i = web.input(id=None)
        if not i.id:
            return json_response({"error": "id not provided"})

        post = db.get_post(i.id)
        if not post:
            return json_response({"error": "post not found"})

        db.delete_post(i.id)
        response = {"status": "created"}
        return json_response(response)

if __name__ == "__main__":
    app.run()
