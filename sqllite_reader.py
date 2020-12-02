import sqlite3
import pandas as pd

con = sqlite3.connect('./database.sqlite')

df = pd.read_sql_query("SELECT * FROM Match;", con)

con.close()

result = df.to_json(r'./match.json', orient="records")
