import random
import time
import mysql.connector
from datetime import datetime, timedelta

# === CONFIGURATION ===
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root1234',  # 🔥 << replace with your real MySQL password
    'database': 'funnelflow'
}

# Funnel steps and their probabilities
FUNNEL_STEPS = [
    ("visit_site", 1.0),        # 100% chance
    ("view_product", 0.7),      # 70% chance
    ("add_to_cart", 0.5),       # 50% chance
    ("start_checkout", 0.3),    # 30% chance
    ("complete_purchase", 0.2)  # 20% chance
]

# === FUNCTIONS ===

def connect_db():
    """Connect to MySQL and return connection + cursor."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    return conn, cursor

def create_user(cursor):
    """Insert a new user and return the user ID."""
    cursor.execute("INSERT INTO users (created_at) VALUES (NOW())")
    return cursor.lastrowid

def simulate_events(cursor, user_id):
    """Simulate funnel events for a single user."""
    current_time = datetime.now()

    for event_name, probability in FUNNEL_STEPS:
        if random.random() <= probability:
            cursor.execute(
                "INSERT INTO events (user_id, event_name, event_time) VALUES (%s, %s, %s)",
                (user_id, event_name, current_time)
            )
            # Slightly increment event times to simulate real behavior
            current_time += timedelta(seconds=random.randint(30, 300))
        else:
            # User drops off at this stage
            break

def simulate_users(num_users):
    """Simulate multiple users through the funnel."""
    conn, cursor = connect_db()

    try:
        for _ in range(num_users):
            user_id = create_user(cursor)
            simulate_events(cursor, user_id)
        
        conn.commit()
        print(f"Successfully simulated {num_users} users.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

# === MAIN ===

if __name__ == "__main__":
    simulate_users(100)  # 🔥 Change number of users here if you want
