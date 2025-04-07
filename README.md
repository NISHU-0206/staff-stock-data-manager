# Staff and Stock Management System (Python)

This project is a Python-based management system that includes:

- Staff Directory creation and storage using CSV files.
- Stock management (purchased and sold) using text files.
- Calculation of remaining stock.
- Calculation of profit percentage per month.
- Bar graph representation of profit percentage using `matplotlib`.

---

## 📁 Modules Used

- `csv` – For handling employee data (staff directory).
- `matplotlib.pyplot` – For plotting bar graphs (profit percentage).
- Basic Python file I/O operations (read/write/append).

---

## 🧾 Features

### 1. Staff Directory using CSV

- Prompts the user to input staff details such as:
  - Employee ID
  - Name
  - Phone Number
  - Email ID
  - Qualifications
  - Salary
- Stores all details in `Staff_details.csv`.

### 2. Stock Management using Text Files

- `Purchased_Stock.txt` is created with:
  - Initial stock for January (user input)
  - Additional stocks for February to June using a custom `ap()` function

- `Stock_Sold.txt` is created similarly with:
  - Initial sold stock for January (user input)
  - Additional stock sold entries using the `ap()` function

### 3. Stock Left Calculation

- Reads values from `Purchased_Stock.txt` and `Stock_Sold.txt`
- Calculates remaining stock = Purchased - Sold
- Displays remaining stock for each month

### 4. Profit Percentage Calculation

- Takes user input for:
  - Cost price per product
  - Selling price per product
- Calculates:
  - Total cost and selling price per month
  - Monthly profit and profit percentage
- Displays profit percentage list

### 5. Graphical Representation

- Plots a bar graph of monthly profit percentage
- Uses `matplotlib.pyplot` to visualize:
  - X-axis → Months
  - Y-axis → Profit percentage

---

## 🔧 How to Run

1. Make sure you have Python installed (preferably Python 3).
2. Install `matplotlib` if not already installed:
pip install matplotlib

3. Save the code into a `.py` file (e.g., `staff_stock_management.py`).
4. Run the file:
python staff_stock_management.py

---

## 📂 Output Files Created

- `Staff_details.csv` – Contains staff records.
- `Purchased_Stock.txt` – Monthly records of purchased stock.
- `Stock_Sold.txt` – Monthly records of sold stock.

---

## 📈 Output (Sample)

After running the code and entering the values, you'll get:

- Printed lists of:
- Purchased stock
- Sold stock
- Remaining stock
- Profit percentage
- A bar graph showing monthly profit percentages.
