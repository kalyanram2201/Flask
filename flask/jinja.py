# Building URL Dynamically
#Variable Rule
#Jinja 2


### Jinja2 Template Engine

'''
{{ }} expression to print html
{%...%} conditional ,for loops,while etc
{#...#} forcomments
'''
##Flask Skelton
from flask import Flask,render_template,request,redirect,url_for
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')


#@app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#     return render_template('/form.html')
## Varibale Rule

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    return render_template('result1.html',results=res)

@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    
    exp={'score':score,"res":res}
    return render_template('result1.html',results=exp)
    
##If condition
@app.route('/successif/<int:score>')
def successif(score):
    
    return render_template('result.html',results=score)
 
 
@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result1.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        sci=float(request.form['science'])
        mat=float(request.form['maths'])
        c=float(request.form['c'])
        ds=float(request.form['datascience'])
        
        total_score=(sci+mat+c+ds)/4
    else:
        return render_template('getresults.html')
    
    return redirect(url_for('successres',score=total_score))



@app.route('/about')
def about():
    return render_template('about.html')
if __name__=="__main__":
    app.run(debug=True)