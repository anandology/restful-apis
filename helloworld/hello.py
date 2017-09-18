import web
import base64

urls = (
    "/", "index",
    "/hello", "hello",
)

app = web.application(urls, globals())

class index:
    def GET(self):
        web.header("Content-Type", "text/plain")
        return "Welcome!\n"

class hello:
    def GET(self):
        i = web.input(name="World")
        web.header("Content-Type", "text/plain")
        return "Hello {}!\n".format(i.name)

if __name__ == "__main__":
    app.run()
