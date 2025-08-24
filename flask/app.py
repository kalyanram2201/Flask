##Flask Skelton
from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the best Flask Course.This should be an amaging course"


@app.route("/index")
def index():
    return "This is an index page"

if __name__=="__main__":
    app.run(debug=True)