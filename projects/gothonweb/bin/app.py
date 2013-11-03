import web

urls = (
        '/hello', 'index'
        )

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class index:
    def GET(self):
        return render.hello_form()

    def POST(self):
        form = web.input(greet="Hello", name="Nobody", datafile={})
        # check for empty strings
        if not form.greet:
            form.greet = "Hello"
        if not form.name:
            form.name = "Nobody"
        greeting = "%s, %s" % (form.greet, form.name)
        filename = form.datafile.filename
        if filename:
            # replace spaces
            filename = filename.replace(' ', '_')
            # escape hashes (otherwise it gets interpretted as python comment)
            filename = filename.replace('#', 'hash')
            # splits the and chooses the last part (the filename with extension)
            filename = filename.split('/')[-1]
            # creates the file where the uploaded file should be stored
            with open('static/'+ filename,'w') as fout:
                # writes the uploaded file to the newly created file.
                fout.write(form.datafile.file.read())
        return render.index(greeting, filename)

if __name__ == "__main__":
    app.run()
