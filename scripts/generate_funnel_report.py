import mysql.connector
import os

# === CONFIGURATION ===
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root1234',  #
    'database': 'funnelflow'
}

REPORTS_FOLDER = 'reports'

# === FUNCTIONS ===

def connect_db():
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn

def get_funnel_data(cursor):
    query = """
    SELECT event_name, COUNT(*) AS total_users
    FROM events
    GROUP BY event_name
    ORDER BY total_users DESC;
    """
    cursor.execute(query)
    return cursor.fetchall()

def get_next_report_number():
    existing = [f for f in os.listdir(REPORTS_FOLDER) if f.startswith('funnel_summary_') and f.endswith('.txt')]
    numbers = []
    for filename in existing:
        try:
            num = int(filename.replace('funnel_summary_', '').replace('.txt', ''))
            numbers.append(num)
        except ValueError:
            continue
    return max(numbers, default=0) + 1

def save_report(data, report_number):
    filename = os.path.join(REPORTS_FOLDER, f"funnel_summary_{str(report_number).zfill(3)}.txt")
    with open(filename, 'w') as f:
        f.write("FunnelFlow Funnel Summary Report\n")
        f.write("Generated Automatically\n\n")
        f.write(f"{'Step':<20} | {'Number of Users'}\n")
        f.write(f"{'-'*20}-+-{'-'*15}\n")
        for event_name, total_users in data:
            f.write(f"{event_name:<20} | {total_users}\n")
    print(f"✅ Report saved as: {filename}")

# === MAIN ===

if __name__ == "__main__":
    conn = connect_db()
    cursor = conn.cursor()
    
    data = get_funnel_data(cursor)
    next_number = get_next_report_number()
    save_report(data, next_number)
    
    cursor.close()
    conn.close()
