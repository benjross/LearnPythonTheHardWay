import web

urls = (
        '/(.*)', 'index'
        )

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
    def GET(self, message):
        #greeting = "Hello World"
        #i = web.input(greeting=None)
        #return render.index(i.greeting)
        return render.index(message)
        #return render.index(greeting = greeting)
        #return render.foo()

if __name__ == "__main__":
    app.run()
