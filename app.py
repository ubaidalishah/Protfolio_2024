from flask import Flask,request,render_template,url_for

app=  Flask(__name__)


@app.route('/')
def home():
    
    return render_template('index.html')
@app.route('/contact')
def contact():
    
    return render_template('contact.html')
@app.route('/projects')
def projects():
    
    return render_template('projects.html')
@app.route('/resume')
def resume():
    
    return render_template('resume.html')


app.run(host="0.0.0.0", debug=True)