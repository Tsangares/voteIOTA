from iota import Iota, ProposedTransaction, Address, TryteString, Fragment, Transaction
from iota.crypto.addresses import AddressGenerator
import math,hashlib,json

# Helper function to get a default api
def getApi(node='https://nodes.iota.org:443') -> Iota:
    return Iota(adapter = node)

# This will convert the vote strings to an IOTA transaction
def getTx(text:str, address:Address) -> ProposedTransaction:
    return ProposedTransaction(
        address = address,
        value = 0,
        message = text
    )

# Taking a string, will post the message to IOTA in a bundle.
# If the string is too big for one transaction,
#  this function will split it into multiple transactions.
# Returns the transaction & bundle hashes
def sendText(message:str, address:Address, api:Iota=None):
    if api is None:
        api = getApi()
    limit = Fragment.LEN
    encode = TryteString.from_unicode
    msg = encode(message)
    txs = math.ceil(len(msg) / limit)
    
    transactions = [getTx(msg[i*limit:(i+1)*limit],address) for i in range(txs)]
    return api.send_transfer(transfers = transactions)['bundle']

# Give it a list of tranction hashes representing votes
# Returns either the dict or list contained in the transaction
def fetchJson(transactions:list):
    #decode converts trytes to json string then parses it to dict or list
    decode = lambda a: json.loads(a.signature_message_fragment.decode())
    if len(hashes)>0:
        transactions = api.get_transaction_objects(hashes)['transactions']
        return [decode(t) for t in transactions]
    return []

# Give the string to a state (e.g. 'California')
# Returns a list of all the transactions as dict objects
def getStateTransactions(state:str) -> list:
    api = getApi()
    address = json.load(open('states.json'))[state]
    hashes=api.find_transactions(addresses=[address,])['hashes']
    return fetchJson(hashes)
    
# Give it all the credentials for a vote, submits vote to ledger
# Retuns transaction hashes
def vote(name:str, identity:str, candidate:str, location:str):
    sha = lambda t: hashlib.sha256(t.encode('utf-8')).hexdigest()
    token={
        'name': name,
        'candidate': candidate,
        'id': identity,
    }
    return sendText(json.dumps(token),Address(location))

# Give it a list of tranction hashes representing votes
# Will return a dict representing a binning of the candidate field
def countVotes(transactions:list):
    votes = fetchJson(transactions)
    for vote in votes:
        print(f"{vote['name']} voted for {vote['candidate']}")
    candidates = [v['candidate'] for v in votes]
    counts = {candidate: candidates.count(candidate) for candidate in candidates}
    return counts

# Loop through each state, fetch transactions and count the votes.
# Returns a dict of each state as key and their binned votes as values
def getStateVotes(states:dict=None):
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

# Takes the output of getStateVotes and totals the votes in a dict.
# Returns a binned dictionary of the candidate's votes.
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
