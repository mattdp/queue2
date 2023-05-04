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
    update_list = [
        (8,"post-call follow up",False),
        (9,"see if new VP is interested",8),
        (12,"wait 6 months",9),
        (5,"send a quote",False)
    ]
    inserts(update_list,connection,table_name)
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
    cursor = connection.execute(f"SELECT * FROM {table_name}")
    for row in cursor:
        print_row(row)

def print_row(row):
    strings = list(map(str,row))
    print(",".join(strings))

def add_tuple(queue,change):
    queue.append(change)
    return 0

def inserts(update_list,connection,table_name):

    for entry in update_list:
        #quotes manually added since middle input a string - there must be be a better way
        #putting in FALSE instead of null seems like a possible future problem, but does seem to revert to 0
        sql = f"INSERT INTO {table_name} (CRM_ID,PAYLOAD,NEXT_ID) VALUES ({entry[0]},'{entry[1]}',{entry[2]})"
        connection.execute(sql)

def process_tuple(queue):
    return queue.pop(0)

main()