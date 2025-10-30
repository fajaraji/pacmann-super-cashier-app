# Super Cashier – PacCommerce Version (Python)

## 1. Background

PacCommerce wants to provide a **self-service cashier** feature so customers can input their own shopping items without depending on a cashier. Customers should be able to:

* add items (name, quantity, price),
* fix wrong inputs (wrong name, wrong quantity, wrong price),
* remove items if they cancel something,
* review the order before paying,
* get the **final price** including **automatic discounts** based on total spending.

To support that, we build a small Python program using OOP. All business logic is placed inside a `Transaction` class (in `transaction.py`), and we test it using `main.py`.

This README documents what the program does, how it works, and how the test cases map to the project brief.

---

## 2. Requirements / Objectives

The program must be able to do these things:

1.  **Create a new transaction**
    * When we create `trx = Transaction()`, it should start with an empty cart.

2.  **Add item**
    * Input: item name, quantity, price per item.
    * Validation: name must not be empty, quantity > 0, price > 0.
    * After adding, program should show the current items (to mimic the sample output in the brief).

3.  **Update item**
    * Update item name (e.g. typo).
    * Update item amount (e.g. quantity was wrong).
    * Update item price (e.g. input price was wrong).

4.  **Delete item**
    * Remove 1 item from the transaction.

5.  **Reset transaction**
    * Remove all items from the cart.

6.  **Check order**
    * Validate that all items have valid data.
    * If valid, show items in a **table** (we use `tabulate`) with columns:
        * Item Name
        * Amount
        * Price/Item
        * Total Price

7.  **Calculate total price**
    * Sum all items.
    * Apply discount based on the rules from the brief:
        * > 200,000 and ≤ 300,000 → 5%
        * > 300,000 and ≤ 500,000 → 8%
        * > 500,000 → 10%
        * otherwise → 0%
    * Show total price, discount percentage, and final price.

---

## 3. Program Flow

Below is the simple flow used in `main.py`:

1.  Customer 1 creates a transaction.
2.  Customer 1 adds 2 items using `add_item(...)`.
3.  Customer 1 deletes one of the items using `delete_item(...)`.
4.  Customer 1 checks the order using `check_order()`.
5.  Customer 1 calculates the total using `total_price()`.
6.  Customer 1 resets the transaction using `reset_transaction()`.
7.  Customer 2 creates a new transaction object.
8.  Customer 2 adds several items, updates quantity, then checks and calculates total.

This flow matches the “add → fix → check → pay” journey in the project document.

---

## 4. Project Structure

.
├── transaction.py     # contains Transaction class (business logic)
└── main.py            # contains test cases / scenario demo

## 5. Class, Attributes, and Methods

### 5.1 Class: Transaction
This class represents one shopping session.

Attribute:

self.items: dict

This structure makes it easy to update just one item.

### 5.2 Methods
#### 5.2.1 add_item(name: str, amount: int, price: float) -> str
Purpose: add a new item to the cart.

Validation: name must not be empty, amount > 0, price > 0.

On success: returns the current items + success message.

On error: returns "Invalid input data."

Example return:

#### 5.2.2 update_item_name(old_name: str, new_name: str) -> str
Rename item (for typo cases).

If old name exists → rename and return success message.

Else → return "Item <old_name> not found."

#### 5.2.3 update_item_amount(name: str, new_amount: int) -> str
Change quantity of an existing item.

Validates new_amount > 0.

If item exists → update.

Else → return "Item <name> not found."

#### 5.2.4 update_item_price(name: str, new_price: float) -> str
Change price of an existing item.

Validates new_price > 0.

If item exists → update.

Else → return "Item <name> not found."

#### 5.2.5 delete_item(name: str) -> str
Remove one item from the cart.

If item exists → delete and return current items.

Else → return "Item <name> not found."

#### 5.2.6 reset_transaction() -> str
Clear all items.

Always returns:

#### 5.2.7 check_order() -> str
Purpose:

check if cart is empty,

check if every item has valid name, amount, and price,

if valid → show table.

If empty:

If invalid data:

If valid: returns a table rendered by tabulate:

#### 5.2.8 total_price() -> str
Purpose: calculate grand total and apply discount.

Discount rules:

200,000 < total ≤ 300,000 → 5%

300,000 < total ≤ 500,000 → 8%

total > 500,000 → 10%

else → 0%

Example output:

## 6. Test Cases
Below are the test cases from main.py, adapted from the project document.

### 6.1 Test Case 1 – Add 2 items
Expected:

both items saved

shows current items

message “Item … added successfully.”

### 6.2 Test Case 2 – Delete an item
Expected:

Toothpaste removed

current items shown

### 6.3 Test Case 3 – Check order + total price
Expected:

if items valid → show table

then show total, discount, final price

### 6.4 Test Case 4 – Reset transaction
Expected:

### 6.5 Test Case 5 – New transaction
Expected: new cart with 3 items.

### 6.6 Test Case 6 – Update item amount
Expected:

### 6.7 Test Case 7 – Check and total
Expected: table + total + discount.

## 7. Conclusion / Future Work
This project successfully covers the requirements from the Pacmann “Super Cashier” brief:

can add, update, delete, and reset items,

can validate order and display it in a table,

can calculate total with discount rules.

Possible improvements:

CLI menu instead of hardcoded test cases,

persistence (save to file / DB),

role-based access for price updates,

unit tests for each method.
