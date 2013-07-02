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
        greeting = "%s, %s" % (form.greet, form.name)
        filename = form.datafile.filename
        if filename:
            # replaces the windows-style slashes with linux ones.
            filepath = form.datafile.filename.replace('\\','/')
            # splits the and chooses the last part (the filename with extension)
            filename = filepath.split('/')[-1]
            # creates the file where the uploaded file should be stored
            fout = open('static/'+ filename,'w')
            # writes the uploaded file to the newly created file.
            fout.write(form.datafile.file.read())
            # closes the file, upload complete.
            fout.close()
        return render.index(greeting, filename)

if __name__ == "__main__":
    app.run()
