import os
import pandas as pd
import mysql.connector

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Read CLEAN data
df = pd.read_csv(os.path.join(BASE_DIR, "data", "hr_cleaned.csv"))

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Uday1707",
    database="hr_analytics"
)


cursor = conn.cursor()

query = """
INSERT INTO hr_attrition VALUES
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for _, row in df.iterrows():
    cursor.execute(query, tuple(row))

conn.commit()
conn.close()

print("STEP 2 DONE: DATA INSERTED INTO MYSQL")
