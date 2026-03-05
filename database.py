import sqlite3

class Database:
    def __init__(self, db_name="gym_app.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS user_profile (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    weight REAL,
                    height REAL
                )
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS workouts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    day TEXT,
                    exercise TEXT,
                    sets INTEGER,
                    reps INTEGER,
                    date TEXT
                )
            """)

    def add_profile(self, name, age, weight, height):
        with self.conn:
            self.conn.execute("INSERT INTO user_profile (name, age, weight, height) VALUES (?, ?, ?, ?)",
                              (name, age, weight, height))

    def get_profile(self):
        cursor = self.conn.execute("SELECT * FROM user_profile")
        return cursor.fetchone()

    def log_workout(self, day, exercise, sets, reps, date):
        with self.conn:
            self.conn.execute("INSERT INTO workouts (day, exercise, sets, reps, date) VALUES (?, ?, ?, ?, ?)",
                              (day, exercise, sets, reps, date))

    def get_workouts(self):
        cursor = self.conn.execute("SELECT * FROM workouts")
        return cursor.fetchall()
