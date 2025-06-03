# 🧮 General Store Billing Software

This is a lightweight, offline billing software designed for Indian general stores. It runs on a single window with a clean interface, allowing store owners to manage items, generate bills with unit-based pricing (grams, liters, pieces), and handle payments including credit tracking.

---

## 📦 Features

* ✅ Single-window UI with sidebar navigation
* ✅ Item management with dropdown for units
* ✅ Unit-based billing (e.g., grams, liters, pieces)
* ✅ Live bill preview with item-wise total
* ✅ Payment methods: **Cash, UPI, Credit**
* ✅ Credit customer tracking & viewing
* ✅ Uses SQLite for data persistence (no internet required)

---

## 🖥️ Requirements

* Python 3.8 or higher
* Tkinter (comes pre-installed with Python)
* OS: Windows, Linux, or macOS

> 💡 No need to install any external packages. All modules (`tkinter`, `sqlite3`, `os`) are built into Python.

On **Linux**, you may need to install Tkinter manually:

```bash
sudo apt-get install python3-tk
```

---

## 📁 File Structure

```
billingSoftware/
├── main_app.py                  # Main application file
├── database.py                  # SQLite database functions
├── data/
│   └── store.db                 # SQLite database file (auto-created)
└── README.md
```

---

## 🚀 How to Run

1. Install Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Clone or download the repo.
3. Open terminal or command prompt in the `billingSoftware/` folder.
4. Run the app:

```bash
python main_app.py
```

---

## 🧰 How to Use

### 🛒 Billing Tab

* Enter the item code, quantity, and select unit.
* Click **Add Item** to add to the bill.
* Select payment method (Cash/UPI/Credit).
* If Credit is selected, you will be prompted for customer name.
* Bill total and item details are displayed live.

### 📦 Manage Items Tab

* Add or update items by entering code, name, price, and selecting unit.
* All items are listed below with pricing info.

### 📋 Credits Tab

* View all credit customer entries.

---

## 💾 Data Files

* Data is now stored in a **SQLite database** (`data/store.db`).
* You can use tools like **DB Browser for SQLite** to inspect or modify data.

---

## 📈 Pointers for Next Steps

Here are some ideas to enhance or scale the software as you continue learning:

* **Error handling & validation** – add validation for user input and handle unexpected input formats.
* **Improving UI** – while Tkinter is easy, it’s basic. You could explore **PyQt**, **Kivy**, or use **Tkinter themes** for a modern look.
* **Packaging** – create a standalone app using **PyInstaller** or **auto-py-to-exe** so shopkeepers don’t need Python installed.
* **Testing** – add basic unit tests using the `unittest` module to prevent bugs when you add features.
* **New features** – such as reports, user accounts, inventory alerts, or billing history.

---

## 💡 Best Devices for Shop Owners (India)

If you don’t have a PC, here are affordable options:

### 💻 Option 1: Budget Laptop (₹20,000–₹30,000)

* Example: [Lenovo IdeaPad 1](https://www.amazon.in/dp/B0B3G85YTR)

### 💡 Option 2: Raspberry Pi 5 + Monitor (₹10,000–₹12,000)

* Perfect for low-budget offline stores

---

## 📃 License

This project is free to use and modify for educational and non-commercial use.

---

## 👨‍💻 Author

**Yaswanth Kumar Gamidi**
GitHub: @yash200508
