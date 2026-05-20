import os
import sqlite3

from werkzeug.security import generate_password_hash

DATABASE = os.path.join(os.path.dirname(__file__), "..", "spendly.db")


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            name          TEXT    NOT NULL,
            email         TEXT    NOT NULL UNIQUE,
            password_hash TEXT    NOT NULL,
            created_at    TEXT    NOT NULL DEFAULT (datetime('now'))
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id     INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            amount      REAL    NOT NULL,
            category    TEXT    NOT NULL,
            date        TEXT    NOT NULL,
            description TEXT,
            created_at  TEXT    NOT NULL DEFAULT (datetime('now'))
        )
    """)
    conn.commit()
    conn.close()


def seed_db():
    conn = get_db()

    existing = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    if existing > 0:
        conn.close()
        return

    conn.execute(
        "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
        ("Demo User", "demo@spendly.com", generate_password_hash("demo123")),
    )
    conn.commit()

    user = conn.execute("SELECT id FROM users WHERE email = ?", ("demo@spendly.com",)).fetchone()
    user_id = user["id"]

    sample_expenses = [
        (user_id, 45.50,  "Food",          "2026-05-01", "Weekly groceries"),
        (user_id, 30.00,  "Transport",     "2026-05-03", "Monthly bus pass"),
        (user_id, 15.99,  "Entertainment", "2026-05-05", "Netflix subscription"),
        (user_id, 120.00, "Bills",         "2026-05-08", "Electricity bill"),
        (user_id, 25.00,  "Shopping",      "2026-05-10", "New t-shirt"),
        (user_id, 60.00,  "Health",        "2026-05-12", "Pharmacy"),
        (user_id, 12.50,  "Food",          "2026-05-15", "Coffee and snacks"),
        (user_id, 8.00,   "Other",         "2026-05-18", "Miscellaneous"),
    ]

    conn.executemany(
        "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
        sample_expenses,
    )
    conn.commit()
    conn.close()
