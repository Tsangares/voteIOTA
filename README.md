# Installation

It is reccomended to use a python virtual environment. Once it is setup, install the dependencies using:

    pip install -r requirements.txt
	
Then you can run the flask server by being the project's root directory and executing the helper command:

	./run
	
# Summary

This project contains a flask app that uses the python files located at `flask/vote` to communicate with the IOTA ledger.

# Context

Currently in the United States the Postmaster of the U.S. Postal Service has been appointed by Donald Trump to [Louis DeJoy](https://www.cbsnews.com/news/louis-dejoy-trump-republican-donor-usps/). In his first acts he has removed worker overtime and [decomissioned 671 high-volume sorting machines](https://www.washingtontimes.com/news/2020/aug/21/dejoy-usps-not-return-decommissioned-sorting/). Because of the upcoming election and also coronavirus, it is expected to have a lot of mail-in voting. There is worry that the U.S. Postal service will be unfit to correctly process the ballots. 

This application is to show the ease of creating an online voting system. By using IOTA this service could be transparent enough to show that fake votes and not being created, and no vote would be lost.

