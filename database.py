import sqlite3
import os

DB_FILE = "data/store.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # Items table
    c.execute('''
        CREATE TABLE IF NOT EXISTS items (
            code TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            price_per_unit REAL NOT NULL,
            unit TEXT NOT NULL
        )
    ''')

    # Credit customers table
    c.execute('''
        CREATE TABLE IF NOT EXISTS credits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            amount_due REAL NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def get_all_items():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM items")
    rows = c.fetchall()
    conn.close()
    return rows

def add_or_update_item(code, name, price, unit):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO items (code, name, price_per_unit, unit)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(code) DO UPDATE SET
            name=excluded.name,
            price_per_unit=excluded.price_per_unit,
            unit=excluded.unit
    ''', (code, name, price, unit))
    conn.commit()
    conn.close()

def get_item_by_code(code):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM items WHERE code=?", (code,))
    row = c.fetchone()
    conn.close()
    return row

def save_credit(name, amount):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO credits (customer_name, amount_due) VALUES (?, ?)", (name, amount))
    conn.commit()
    conn.close()

def get_all_credits():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT customer_name, amount_due FROM credits")
    rows = c.fetchall()
    conn.close()
    return rows
