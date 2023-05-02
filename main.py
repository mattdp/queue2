import sqlite3

#underlying assumption: table called QUEUE

def main():
    queue = [(1,"remove spanner"),(5,"reticulate splines"),(8,"polish vortices")]

    add_tuple(queue,(89,"sample addition"))
    process_tuple(queue)
    print(queue)

    connection = sqlite3.connect('first.db')
    table_name = "QUEUE"

    wipe_table(connection,table_name)
    #FIX: underlying assumption: table called QUEUE
    connection.execute("INSERT INTO QUEUE (CRM_ID,PAYLOAD,NEXT_ID) VALUES (8,'The first insertion',NULL)")
    print_table(connection,table_name)

    return 0

#not called unless making a change to table structure
#underlying assumption: table called QUEUE
def initialize_schema():
    connection.execute("DROP TABLE QUEUE")

    table_creation_text = '''
    CREATE TABLE IF NOT EXISTS QUEUE
    (CRM_ID      TEXT                    NOT NULL,
    PAYLOAD     TEXT                    NOT NULL,
    NEXT_ID     INT);
    '''

    connection.execute(table_creation_text)

# deliberately delete all entries from table
def wipe_table(connection,table_name):
    connection.execute(f"DELETE FROM {table_name}")

def print_table(connection,table_name):
    cursor = connection.execute("SELECT * FROM QUEUE")
    for row in cursor:
        print_row(row)

def print_row(row):
    strings = list(map(str,row))
    print(",".join(strings))

def add_tuple(queue,change):
    queue.append(change)
    return 0

def process_tuple(queue):
    return queue.pop(0)

main()