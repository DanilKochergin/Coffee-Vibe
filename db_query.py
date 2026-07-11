import sqlite3
import json
import sys

DB_PATH = r"C:\Users\danil\.local\share\mimocode\mimocode.db"
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# 1. List tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [r[0] for r in cur.fetchall()]
print("=== TABLES ===")
print(tables)

# 2. List sessions (newest first)
cur.execute("SELECT id, project_id, session_id, directory, title, time_created FROM session ORDER BY time_created DESC")
sessions = cur.fetchall()
print("\n=== SESSIONS (newest first) ===")
for s in sessions:
    print(dict(s))

# 3. List projects
cur.execute("SELECT DISTINCT project_id FROM session")
projects = [r[0] for r in cur.fetchall()]
print("\n=== PROJECTS ===")
print(projects)

conn.close()
