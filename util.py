from iota import Iota, ProposedTransaction, Address, TryteString, Fragment
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
