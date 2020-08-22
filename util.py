from iota import Iota, ProposedTransaction, Address, TryteString, Fragment, Transaction
from iota.crypto.addresses import AddressGenerator
import math,hashlib,json

def getApi():
    return Iota(adapter = 'https://nodes.iota.org:443')
def getTx(text,address):
    return ProposedTransaction(
        address = address,
        value = 0,
        message = text
    )
def sendText(message,address,api=None):
    if api is None:
        api = getApi()
    limit = Fragment.LEN
    encode = TryteString.from_unicode
    msg = encode(message)
    txs = math.ceil(len(msg) / limit)
    
    transactions = [getTx(msg[i*limit:(i+1)*limit],address) for i in range(txs)]
    return api.send_transfer(transfers = transactions)['bundle']

def vote(name,identity,candidate,location):
    sha = lambda t: hashlib.sha256(t.encode('utf-8')).hexdigest()
    token={
        'name': name,
        'candidate': candidate,
        'id': identity,
    }
    return sendText(json.dumps(token),Address(location))


def countVotes(transactions):
    getVote = lambda a: json.loads(a.signature_message_fragment.decode())
    votes = [getVote(transaction) for transaction in transactions]
    for vote in votes:
        print(f"{vote['name']} voted for {vote['candidate']}")
    candidates = [v['candidate'] for v in votes]
    counts = {candidate: candidates.count(candidate) for candidate in candidates}
    return counts

def getStateVotes(states=None):
    api = getApi()
    if states is None:
        with open('states.json','r') as f:
            states = json.load(f)
    counts = {}
    for name,address in states.items():
        hashes=api.find_transactions(addresses=[address,])['hashes']
        if len(hashes) > 0:
            transactions = api.get_transaction_objects(hashes)['transactions']
            votes = countVotes(transactions)
            counts[name] = votes
            print(name,votes)
            
    return counts

def totalVotes(states):
    total = {}
    for state,votes in states.items():
        for candidate,count in votes.items():
            if candidate not in total:
                total[candidate] = 0
            total[candidate] += count
    return total
if __name__ == "__main__":
    api = getApi()

