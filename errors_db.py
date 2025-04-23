import sqlite3

def create_database():
    conn = sqlite3.connect("errors.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS errors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            error_message TEXT UNIQUE,
            solution TEXT
        )
    """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("✅ Database 'errors.db' initialized successfully!")

