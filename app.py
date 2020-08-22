from flask import Flask,render_template,request
import json
from util import *
app = Flask(__name__)



@app.route('/')
def hello_world():
    locations = json.load(open('states.json'))
    tally = json.load(open('votes.json'))
    total = totalVotes(tally)
    return render_template('index.html',locations=locations.items(),tally=tally.items(),total=total.items())


@app.route('/vote',methods=["POST"])
def voting():
    name = request.form['name']
    identity = request.form['id']
    candidate = request.form['candidate']
    state = request.form['location']
    locations = json.load(open('states.json'))
    location = locations[state]
    transaction = vote(name,identity,candidate,location).transactions[0].hash
    tally = json.load(open('votes.json'))
    if candidate not in tally[state]:
        tally[state][candidate]=1
    else:
        tally[state][candidate]+=1
    json.dump(tally,open('votes.json','w+'))
    total = totalVotes(tally)
    return render_template('vote.html',name=name,identity=identity,candidate=candidate,location=location,transaction=transaction,tally=tally.items(),total=total.items())

@app.route('/addresses', methods=['GET'])
def addresses():
    with open('states.json','r') as f:
        locations = json.load(f)
    return str(locations)

@app.route('/tally', methods=['GET'])
def tally():
    state = request.args.get('state',None)
    tally = None
    if state is None:
        tally = json.load(open('votes.json'))
    else:
        states = json.load(open('states.json'))
        tally = getStateVotes({state: states[state]})
        votes = json.load(open('votes.json'))
        votes[state] = tally[state]
        json.dump(votes,open('votes.json','w+'))
    return tally
