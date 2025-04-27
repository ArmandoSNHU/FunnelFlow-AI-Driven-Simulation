# FunnelFlow: AI-Driven Customer Journey Simulation

**FunnelFlow** is a lightweight simulation and analysis project that models customer behavior through a sales funnel.  
It uses a MySQL database, Python-based AI user agents, and auto-generated reports to track and analyze conversion steps.

---

## 📦 Project Structure

```
FunnelFlow-Ai-Driven-Simulation/
│
├── sql/
│   └── create_tables.sql           # Database schema
│
├── scripts/
│   ├── simulate_users.py           # AI agent to simulate user events
│   ├── generate_funnel_report.py   # Auto-generate funnel reports
│
├── tests/
│   └── validate_funnel.sql         # SQL scripts to verify data
│
├── reports/
│   └── funnel_summary_001.txt      # Auto-generated reports (txt, csv)
│
├── notes/
│   └── analysis_plan.md            # Analysis and design notes
│
└── README.md                       # Project overview
```

---

## ⚙️ How It Works

1. **Database**:  
   - `users` table records each simulated user.
   - `events` table records funnel actions like "visit site", "view product", "add to cart", etc.

2. **AI Simulation**:  
   - `simulate_users.py` creates fake users and events with realistic drop-off probabilities.

3. **Auto-Reporting**:  
   - `generate_funnel_report.py` queries the database and saves a numbered text report to `/reports/`.
   - Each run creates a new, incremented report file (ex: `funnel_summary_002.txt`).

---

## 🛠 Setup Instructions

### 1. Install Requirements
```bash
pip install mysql-connector-python
```

### 2. Setup MySQL Database
```bash
mysql -u root -p < sql/create_tables.sql
```
(Enter your MySQL root password when prompted.)

### 3. Update Python Scripts
Inside `simulate_users.py` and `generate_funnel_report.py`, edit your database config:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_mysql_password',
    'database': 'funnelflow'
}
```

### 4. Simulate Users
```bash
python scripts/simulate_users.py
```
(Generates fake users and funnel activity.)

### 5. Generate Funnel Report
```bash
python scripts/generate_funnel_report.py
```
(Automatically saves a new funnel report inside `/reports/`.)

---

## 📈 Example Funnel Steps

| Step             | Probability |
|------------------|-------------|
| visit_site       | 100%         |
| view_product     | 70%          |
| add_to_cart      | 50%          |
| start_checkout   | 30%          |
| complete_purchase| 20%          |

Each step simulates realistic user drop-off.

---

## 💡 Future Enhancements (Ideas)

- Auto-generate `.csv` reports alongside `.txt`
- Add cohort analysis (e.g., simulate different user types)
- Visualize funnel drop-offs with Matplotlib or Chart.js
- Expand funnel steps with custom events

---

## 🧠 Skills Demonstrated

- MySQL database design and queries
- Python database automation
- AI-driven simulation modeling
- Report generation and file management
- Clean project structuring and documentation

---

## 📚 License

This project is for educational and portfolio purposes.

---
