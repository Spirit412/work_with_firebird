from functools import lru_cache
from config import dsn_selex, user_selex, password_selex, database_selex
import fdb
import os.path

SERVER = "localhost"
DATABASE = "Selex.fdb"
PORT = 3054
USER = "SYSDBA"
PASSWORD = "masterkey"
charset = "UTF8"
print(f"File Selex.fdb exists: {os.path.exists(DATABASE)}")


con = fdb.connect(
    database=database_selex,
    user=user_selex,
    password=password_selex,
    charset="UTF8",
    sql_dialect=3,
    no_db_triggers=False,
)

cur = con.cursor()
# query = "SELECT * FROM FZL"


@lru_cache(maxsize=None)
def get_query_fetchall(query):
    cur.execute(query)
    return cur.fetchall()


@lru_cache(maxsize=None)
def get_cur_query(query):
    cur.execute(query)
    return cur


@lru_cache(maxsize=None)
def all_tables() -> list[str]:
    schema = fdb.schema.Schema()
    schema.bind(con)
    return [t.name for t in schema.tables]


@lru_cache(maxsize=None)
def get_columns(col):
    cur.execute("SELECT * FROM %s" % col)
    return cur


columns = [column[0] for column in get_columns("FZL").description]
columns_types = [column[1] for column in get_columns("FZL").description]

result = cur.fetchall()

print("#" * 10)
print(dict(zip(columns, result[0])))
print("#" * 10)
print(dict(zip(columns, columns_types)))
print("#" * 10)
print(all_tables())
print("#" * 10)

def get_all_events():
    cur.execute("SELECT event_name, param FROM 'firebase-public-project.analytics_153293282.events_20181003', UNNEST(event_params) as param WHERE event_name = 'level_complete_quickplay'")
    return cur

all_events = get_all_events()
result = cur.fetchall()

for event in get_all_events():
    print(event)
    
for res in result:
    print(res)


con.commit()
con.close()
