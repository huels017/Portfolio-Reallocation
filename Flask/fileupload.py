from flask import Flask, request, render_template,url_for,send_file
import os

##FLASK##
#In flask you use @app.route() to define a route on your server.
#The fuctions after run after the route is exucuted.
#at the end for the functions you need to return render_templates. 
#this returnes a file located in /var/www/FlaskApp/FlaskApp/Templates.
#the variables defied after it are ones on the html page.

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) #This gets the path of the folder to store the uploaded files in.

def modifications(name): #This Function writes to the file. I made it not tied to a route so can be called at anytime in the code.
    save_path = "/home/share/FlaskApp/txtfiles"
    complete = os.path.join(save_path, name)
    with open(complete, 'w') as file:
        file.write('This file has been modified')
    
@app.route("/")#This displays the index padge. I want to make this padge the homme padge and create a diffrent upload route.
def index():
    return render_template("upload.html")

@app.route("/upload", methods =['GET','POST']) #This is what happens when going to /upload
def upload():
    if request.method == 'GET': #If you go to /upload without submitting files you will be presented with a notallowed.html
        return render_template("notallowed.html")
    else:
            #Might want to change this to a if == 'POST' need to look into it more but it works now just might not be best practice
        target = os.path.join(APP_ROOT, 'txtfiles/')
        list_of_files = [] #Appending the file name to a list will allow us to display those files in html
                              # using a for loop.
        if not os.path.isdir(target):
            os.mkdir(target) # makes the txtfiles directory if ones not present.

        for file in request.files.getlist("file"): #This grabs the files from html
            filename = file.filename
            destination = "/".join([target, filename]) 
            file.save(destination) # saves the file to /txtfiles
            list_of_files.append(filename) #This appends the file name to a list so after the upload Html can display 
                                            #all the files they uploaded.
            for name in list_of_files: 
                modifications(name) #Runs the modifications function(This can go anyware after the files have been uploaded)

        return render_template("complete.html",list = list_of_files) #Displays the complete html with all the names of the files.
                                                                       # list is used in the html file
@app.route("/return-file/")
def return_file(): ##This is a work in progress. Right now it returns the sample.txt but I need to some how store the users uploaded
    return send_file("/home/share/FlaskApp/txtfiles/sample.txt") #Files paths and allow them to download them. I might modify the 
                                                                  #above function to do this dont know yet.
if __name__ == "__main__": 
    app.run(host = "0.0.0.0", port = 33, debug = True) #This runs the server on the local host on port 33. debug alows me to view
                                                        #error codes.
