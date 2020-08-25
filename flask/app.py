from flask import Flask,render_template,request
import json,os
from vote import *

app = Flask(__name__)

VOTES_PATH = os.path.join(os.getcwd(),'flask/vote/votes.json')
STATES_PATH = os.path.join(os.getcwd(),'flask/vote/states.json')


@app.route('/')
def hello_world():
    locations = json.load(open(STATES_PATH))
    tally = json.load(open(VOTES_PATH))
    total = totalVotes(tally)
    return render_template('index.html',locations=locations.items(),tally=tally.items(),total=total.items())

@app.route('/vote',methods=["POST"])
def voting():
    name = request.form['name']
    identity = request.form['id']
    candidate = request.form['candidate']
    state = request.form['location']
    locations = json.load(open(STATES_PATH))
    location = locations[state]
    transaction = vote(name,identity,candidate,location).transactions[0].hash
    tally = json.load(open(VOTES_PATH))
    if state not in tally:
        tally[state] = {}
    if candidate not in tally[state]:
        tally[state][candidate]=1
    else:
        tally[state][candidate]+=1
    json.dump(tally,open(VOTES_PATH,'w+'))
    total = totalVotes(tally)
    return render_template('vote.html',name=name,identity=identity,candidate=candidate,location=location,transaction=transaction,tally=tally.items(),total=total.items())

@app.route('/tally', methods=['GET'])
def tally():
    state = request.args.get('state',None)
    tally = None
    if state is None:
        tally = json.load(open(VOTES_PATH))
    else:
        states = json.load(open(STATES_PATH))
        tally = getStateVotes({state: states[state]})
        votes = json.load(open(VOTES_PATH))
        votes[state] = tally[state]
        json.dump(votes,open(VOTES_PATH,'w+'))
    return tally

@app.route('/transactions',methods=['GET'])
def state_transactions():
    state = request.args.get('state',None)
    if state is None:
        return []
    txs = getStateTransactions(state)
    data = str([{'name': tx['name'], 'candidate': tx['candidate'], 'id': tx['id']} for tx in txs])
    return data

@app.route('/addresses', methods=['GET'])
def addresses():
    with open(STATES_PATH,'r') as f:
        locations = json.load(f)
    return str(locations)

