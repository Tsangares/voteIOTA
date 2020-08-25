# Installation

It is recommended to use a python virtual environment. Once it is setup, install the dependencies using:

    pip install -r requirements.txt
	
Then you can run the flask server by being the project's root directory and executing the helper command:

	./run
	
# Summary

This project contains a flask app that uses the python file located at `flask/vote/vote.py` to communicate with the IOTA ledger.

There is a live version of this application located at https://vote.ekay.com/

# Context

Currently in the United States the Postmaster of the U.S. Postal Service has been appointed by Donald Trump to [Louis DeJoy](https://www.cbsnews.com/news/louis-dejoy-trump-republican-donor-usps/). In his first acts he has removed worker overtime and [decomissioned 671 high-volume sorting machines](https://www.washingtontimes.com/news/2020/aug/21/dejoy-usps-not-return-decommissioned-sorting/). Because of the upcoming election and also coronavirus, it is expected to have a lot of mail-in voting. There is worry that the U.S. Postal service will be unfit to correctly process the ballots. 

# Purpose

This application is to show the ease of creating an online voting system utilizing DLT for security and transparency. By using IOTA this program is able to easily be both public and immutable, allowing no vote to be lost. The whole voting aspect is extremely straightforward; the main challenge with this approach to the voting system is the identity portion of the vote. In this proof of concept, I simply hash a passphrase that holds as the identity of the user. To use this application in a more secure way, the identity needs to hold ideally the following three utilities:

 - Unique to each registered voter
 - Verifiable by either the public or the government
 - Non-duplicative
 
Potentially the identity could be as simple as a social security number. This application only uses hashes, but we could also use public/private key encryption and simply integrate government issued public keys into the application.

The best approach would be an identity verification on a government website or the DMV that takes several forms of identity (like the Real ID application), and it will issue a certificate on the ledger. This certificate can be as simple as a cryptographic signature from the US government on an IOTA address owned by the user. In order for the user to prove ownership of the address and prove that they are a registered voter, they simply spend from the address to two output addresses, one that they own (so they can spend it again), and to the voting platform issuing a verifiable vote by not only the U.S. Government, but also the public.

This could be expanded on in so many ways and varieties. But ultimatley, voting with the ledger is extremely easy and opens so many doors for a secure voting platform.
