import sqlite3

def insert_error(error_message):
    """Insert extracted errors into the database if they are not already stored."""
    conn = sqlite3.connect("errors.db")
    cursor = conn.cursor()

    cursor.execute("INSERT OR IGNORE INTO errors (error_message, solution) VALUES (?, ?)", 
                   (error_message, "No solution yet. Needs manual entry."))

    conn.commit()
    conn.close()

def get_solution(error_message):
    """Retrieve stored solutions for errors."""
    conn = sqlite3.connect("errors.db")
    cursor = conn.cursor()

    cursor.execute("SELECT solution FROM errors WHERE error_message LIKE ?", ('%' + error_message + '%',))
    result = cursor.fetchone()
    
    conn.close()
    
    return result[0] if result else "No solution found. Please check documentation."

if __name__ == "__main__":
    # Read errors from errors.log and insert into the database
    try:
        with open("errors.log", "r") as file:
            for line in file:
                error_text = line.strip()
                insert_error(error_text)

        print("✅ Errors from errors.log stored in the database!")

    except FileNotFoundError:
        print("⚠ No errors.log file found. Run Perl script first.")

    # Start interactive CLI
    while True:
        user_input = input("\nEnter an error message (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break

        solution = get_solution(user_input)
        print(f"\nSuggested Fix: {solution}")

