import sqlite3
import pandas as pd

con = sqlite3.connect('./database.sqlite')

df = pd.read_sql_query("SELECT * FROM Player_Attributes;", con)

con.close()

result = df.to_csv(r'./player_attr.csv', index=False)
