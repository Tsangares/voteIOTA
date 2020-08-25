from util import *
import json

if __name__=="__main__":
    with open('votes.json','w+') as f:
        counts = getStateVotes()
        json.dump(counts,f)

