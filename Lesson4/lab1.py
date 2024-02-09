import sqlite3

con = sqlite3.connect("test.db")
cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS people (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age INTEGER
);
""")
# cursor.execute("INSERT INTO people(name, age) values ('Tom', 38)")
# con.commit()

# people = [("Sam", 28), ("Alice", 33), ("Kate", 25)]
# cursor.executemany("INSERT INTO people (name,age) values (?,?)", people)
# con.commit()

data = cursor.execute("SELECT * FROM people")
# print(data.fetchall())
# print(data.fetchmany())
print(data.fetchone())
