from flask import Flask,render_template,request
import json
from util import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    with open('states.json','r') as f:
        locations = json.load(f)
    return render_template('index.html',locations=locations)


@app.route('/vote',methods=["POST"])
def voting():
    name = request.form['name']
    identity = request.form['id']
    candidate = request.form['candidate']
    location = request.form['location']
    transaction = vote(name,identity,candidate,location).transactions[0].hash
    return render_template('vote.html',name=name,identity=identity,candidate=candidate,location=location,transaction=transaction)
