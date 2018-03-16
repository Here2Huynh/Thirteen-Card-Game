#Postgres Interals

#sql order by command
You can choose columns in the SELECT with ORDER by query like so: SELECT col_1, col_2 FROM example ORDER BY col_1.

#information_schema.tables
conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()

cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' ORDER BY table_name")
for table_name in cur.fetchall():
    name = table_name[0] #unpack the tuple
    print(name)

#.
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
#for table in cur.fetchall():
    # Enter your code here...
from psycopg2.extensions import AsIs

conn = psycopg2.connect(dbname="dq", user="hud_admin", password="eRqg123EEkl")
cur = conn.cursor()

cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
for table in cur.fetchall():
    table = table[0]
    cur.execute("SELECT * FROM %s LIMIT 0", [AsIs(table)])
    print(cur.description, "\n")
