# 🧮 General Store Billing Software

This is a lightweight, offline billing software designed for Indian general stores. It runs on a single window with a clean interface, allowing store owners to manage items, generate bills with unit-based pricing (grams, liters, pieces), and handle payments including credit tracking.

---

## 📦 Features

- ✅ Single-window UI with sidebar navigation
- ✅ Item management with dropdown for units
- ✅ Unit-based billing (e.g., grams, liters, pieces)
- ✅ Live bill preview with item-wise total
- ✅ Payment methods: **Cash, UPI, Credit**
- ✅ Credit customer tracking & viewing
- ✅ CSV file-based data storage (no internet required)

---

## 🖥️ Requirements

- Python 3.8 or higher
- Tkinter (comes pre-installed with Python)
- OS: Windows, Linux, or macOS

---

## 📁 File Structure

billingSoftware/
├── main_app.py # Main application file
├── data/
│ ├── items.csv # Item data (auto-created)
│ └── credit_customers.csv # Credit data (auto-created)
└── README.md


---

## 🚀 How to Run

1. Install Python: https://www.python.org/downloads/
2. Clone or download the repo.
3. Open terminal or command prompt in the `billingSoftware/` folder.
4. Run the app:

```bash
python main_app.py
