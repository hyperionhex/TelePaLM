import sqlite3

def initialize_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('user_history.db')
    cursor = conn.cursor()

    # Create the user_history table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_history (
            user_id TEXT PRIMARY KEY,
            context TEXT
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def save_user_context(user_id, context):
    # Connect to the SQLite database
    conn = sqlite3.connect('user_history.db')
    cursor = conn.cursor()

    # Save the user's context to the database
    cursor.execute('REPLACE INTO user_history (user_id, context) VALUES (?, ?)', (user_id, context))
    conn.commit()

    # Close the database connection
    conn.close()

def get_user_context(user_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('user_history.db')
    cursor = conn.cursor()

    # Retrieve the user's context from the database
    cursor.execute('SELECT context FROM user_history WHERE user_id=?', (user_id,))
    row = cursor.fetchone()

    # If the user exists in the database, retrieve the context
    if row:
        context = row[0]
    else:
        context = ''

    # Close the database connection
    conn.close()

    return context
