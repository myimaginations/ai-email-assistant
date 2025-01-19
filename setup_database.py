import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('database/feedback.db')
cursor = conn.cursor()

# Create a table for storing feedback
cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email_content TEXT NOT NULL,
    predicted_urgency TEXT NOT NULL,
    suggested_response TEXT NOT NULL,
    user_feedback TEXT
)
''')

print("Database and table created successfully!")

# Close the connection
conn.close()
