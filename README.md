# update-scheduler

DONE V1: no HTTP, just internal script logic making a queue of changes
DONE V2: connect to a local DB that's blank or cluttered and make a single change
V3: store queue of changes in a DB table + be able to access them in order
    DONE method to wipe entries in table
    method to store set of tuples in table
    given a tuple, find the next tuple in sequence assuming it exists
    error if it doesn't exist
    method to print info of a set of sequential entries in a queue
V4: tests of what full logic should be able to do w/i DB - output is txt
V5: get it off my machine and into the cloud, including a DB
V6: HTTP inputs so can curl to it
(stop here)
V7: in future, connect output to CRM of choice to run the updates, including checking if update + doing retry logic