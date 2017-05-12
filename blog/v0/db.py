import web

db = web.database(dbn="sqlite", db="blog.db")

def get_posts():
    return db.select("post").list()

def get_post(post_id):
    return db.where("post", id=post_id).first()

def create_post(title, body):
    post_id = db.insert("post", title=title, body=body)
    return post_id

def update_post(post_id, title, body):
    return db.update("post", title=title, body=body,
        where="id=$post_id",
        vars={"post_id": post_id})

def delete_post(post_id):
    return db.delete("post",
        where="id=$post_id",
        vars={"post_id": post_id})
