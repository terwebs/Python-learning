import sqlite3

people_values = (
    ('Webster', 'Human', 26),
    ('Jean', 'Meat Popsicle', 28),
    ("Ernesto's", 'Mangalore', 30)
    )
    

with sqlite3.connect('roster.db')as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(FirstName TEXT, Especies TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", people_values)

    c.execute("SELECT FirstName, IQ FROM Roster WHERE Especies = 'Human'")

    for row in c.fetchall():
        print row
