# import the Flask class from the flask module
from flask import Flask, render_template, request
import ast, os, time
import datetime


# create the application object
app = Flask(__name__)
posts = []

@app.route('/index')
def index():
    with open("WebUserDB.txt", "r") as dbfile:
        if(os.path.getsize("WebUserDB.txt") <= 0): #Check if size of file is less than or equal to 0 - empty file if so
            return render_template("index.html", posts=[]) #Return a blank index page if there are no posts
        else:
            posts=[]
            for line in dbfile:
                posts.append(ast.literal_eval(line)) #Evaluating the string representation of the dictionary from the text file and converting to dict
                                                   #Solves 'str object' has no attribute 'author'
            dbfile.close()
            return render_template("index.html", title='Home', posts=posts)

@app.route('/postAnonComment', methods=['POST'])
def SaveDetails():

    '''INSERT JAVASCRIPT VALIDTION FOR THE TEXTFIELDS!!'''
    '''insert Javascript function to only show last five comments!'''

    userName = request.form['user_name']
    userMail = request.form['user_mail']
    userMessage = request.form['user_message']
    imgOption = request.form['avatar']
    #time = "Posted on " + str(datetime.now().day) + "/" + str(datetime.now().month) + " at: " +  str(datetime.now().hour) + ":" + str(datetime.now().minute)
    time2 = datetime.datetime.utcnow().strftime("Posted %d/%b/%y - %H:%M")

    if(imgOption == "avatar1"):
        imgOption = "static\\avOne.jpg"
    elif(imgOption == "avatar2"):
        imgOption = "static\\avTwo.jpg"
    elif (imgOption == "avatar3"):
        imgOption = "static\\avThree.jpg"
    elif (imgOption == "avatar4"):
        imgOption = "static\\avFour.jpg"
    elif (imgOption == "avatar5"):
        imgOption = "static\\avFive.jpg"
    else:
        imgOption = "static\\avSix.jpg"

    newDictionaryItem = {'avatar': imgOption, 'author': {'nickname': userName},'email': userMail, 'body': userMessage,
                         'postTime': time2}
    dbfile = open("WebUserDB.txt", "a")
    if (os.path.getsize("WebUserDB.txt") <= 0):
        dbfile.write(str(newDictionaryItem))
    else:
        dbfile.write("\n" + str(newDictionaryItem))

    with open("WebUserDB.txt", "r") as dbfile:
        posts = []
        for line in dbfile:
            posts.append(ast.literal_eval(line))  # Evaluating the string representation of the dictionary from the text file and converting to dict
            # Solves 'str object' has no attribute 'author'
        dbfile.close()


    return render_template("index.html", title="Home", posts=posts) #why isnt this reloading the page with all the comments

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
