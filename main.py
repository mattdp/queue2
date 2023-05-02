import sqlite3

#underlying assumption: table called QUEUE

connection = sqlite3.connect('first.db')

connection.execute("DROP TABLE QUEUE")

table_creation_text = '''
CREATE TABLE IF NOT EXISTS QUEUE
(CRM_ID      TEXT                    NOT NULL,
PAYLOAD     TEXT                    NOT NULL,
NEXT_ID     INT);
'''

connection.execute(table_creation_text)

connection.execute("INSERT INTO QUEUE (CRM_ID,PAYLOAD,NEXT_ID) VALUES (8,'The first insertion',NULL)")

cursor = connection.execute("SELECT * FROM QUEUE")
for row in cursor:
    print("CRM_ID = ", row[0])

queue = [(1,"remove spanner"),(5,"reticulate splines"),(8,"polish vortices")]

def main():
    add_tuple((89,"sample addition"))
    process_tuple()
    wipe_table(connection,"QUEUE")
    print(queue)
    return 0

# deliberately delete all entries from table
def wipe_table(connection,table_name):
    connection.execute(f"DELETE FROM {table_name}")

def add_tuple(change):
    queue.append(change)
    return 0

def process_tuple():
    return queue.pop(0)

main()