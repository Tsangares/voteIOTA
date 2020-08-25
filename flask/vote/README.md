# Summary

In this directory are the main IOTA utilities and the data files `states.json` and `votes.json`.

# `states.json`

This file contains the IOTA addresses for each state. The reason each state has its own address is for organization.

# `votes.json`

This file is a cache of the votes on the IOTA ledger. As people vote, this file is updated. If there is a discrepancy between the votes in this file and the ledger simply run `countVotes.py`.

# `countVotes.py`

This file will count the votes for each state and update the `votes.json` file to be accurate with the ledger. The helper file `countVotes.py` also will show you the names of the votes for each state. To run, go into this directory and run:

    python countVotes.py
	
# `generateStates.py`

This file will generate new addresses for each state. It will overwrite the `states.json` with new addresses to reset the votes. To run, go into this directory and run:

    python generateStates.py
