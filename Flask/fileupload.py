from flask import Flask, request, render_template,url_for,send_file
import os
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def modifications(name):
    save_path = "/home/share/FlaskApp/txtfiles"
    complete = os.path.join(save_path, name)
    with open(complete, 'w') as file:
        file.write('This file has been modified')
    


@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods =['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template("notallowed.html")
    else:

        target = os.path.join(APP_ROOT, 'txtfiles/')
        list_of_files = [] #Appending the file name to a list will allow us to display those files in html
                              # using a for loop.
        if not os.path.isdir(target):
            os.mkdir(target)

        for file in request.files.getlist("file"):
            filename = file.filename
            destination = "/".join([target, filename])
            file.save(destination)
            list_of_files.append(filename)

            for name in list_of_files: 
                modifications(name)

        return render_template("complete.html",list = list_of_files)
@app.route("/return-file/")
def return_file():
    return send_file("/home/share/FlaskApp/txtfiles/sample.txt")
       
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 33, debug = True)
