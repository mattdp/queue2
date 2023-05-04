# update-scheduler

DONE V1: no HTTP, just internal script logic making a queue of changes
DONE V2: connect to a local DB that's blank or cluttered and make a single change
V3: store queue of changes in a DB table + be able to access them in order
    DONE method to wipe entries in table
    DONE method to print the table (added row printer)
    DONE method to store set of tuples in table
    given a tuple, find the next tuple in sequence assuming it exists
        since CRM_ID should take letters and numbers, should have a row ID referencable by next_id - feels like there's something under the hood to find there, but how would i know that upon creating the input? definitely making this a linked list for the programming challenge vs. the actual use case here, unclear why ordering should matter aside from multiple edits to the same CRM entry 
            could log the datetime and sort by old to new when attempting updates - https://pynative.com/python-sqlite-date-and-datetime/
                would then drop table and use different schema - no next_id, but do use timestamp
    add status (untried,complete,errored); print info of an ordered set of entries to try updating
V4: tests of what full logic should be able to do w/i DB - output is txt
    overlapping changes to same ID
    attempting to change ID that doesn't exist
    passing in bad values
V5: get it off my machine and into the cloud, including the DB
V6: HTTP inputs so can curl to it
(stop here until concrete personal use - could do more with erroring if want to)
V7: in future, connect output to CRM of choice to run the updates, including checking if update + doing retry logic