
from iota import Iota, ProposedTransaction, Address, TryteString, Fragment
from iota.crypto.addresses import AddressGenerator
from util import *
import math,hashlib,random
api = getApi()
response = api.get_node_info()
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ9"
seed = ''.join(random.choice(letters) for i in range(60))
generator = AddressGenerator(seed.encode('utf-8'))
addresses = generator.get_addresses(start=0,count=50)
states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
]

with open('states.json','w+') as f:
    out = [{'name': state, 'address': str(addr)} for state,addr in zip(states,addresses)]
    json.dump(out,f)





