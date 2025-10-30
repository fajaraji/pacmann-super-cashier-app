# import library
from tabulate import tabulate

# create class
class Transaction:
    def __init__(self):
        self.items = {} # {"name": {"amount": int, "price": float}}

    def add_item(self, name: str, amount: int, price: float):
        if not name or amount <= 0 or price <= 0:
            return "Invalid input data."
        self.items[name] = {"amount": amount, "price": price}
        return f"Current Items: {self.items} \nItem {name} added successfully."
    
    def update_item_name(self, old_name: str, new_name: str):
        if old_name in self.items:
            self.items[new_name] = self.items.pop(old_name)
            return f"Item name updated from {old_name} to {new_name}."
        return f"Item {old_name} not found."
    
    def update_item_amount(self, name: str, new_amount: int):
        if new_amount <= 0:
            return "Invalid amount."
        
        if name in self.items:
            self.items[name]["amount"] = new_amount
            return f"Item {name} amount updated to {new_amount}."
        return f"Item {name} not found."
    
    def update_item_price(self, name: str, new_price: float):
        if new_price <= 0:
            return "Invalid price."

        if name in self.items:
            self.items[name]["price"] = new_price
            return f"Item {name} price updated to {new_price}."
        return f"Item {name} not found."
    
    def delete_item(self, name: str):
        if name in self.items:
            del self.items[name]
            return f"Item {name} deleted successfully. \nCurrent Items: {self.items}"
        else:
            return f"Item {name} not found."
    
    def reset_transaction(self):
        self.items.clear()
        return "Transaction reset successfully."
    
    def check_order(self):
        if not self.items:
            return "No items in the transaction."
        
        for name, details in self.items.items():
            amount = details["amount"]
            price = details["price"]
            
            if not (name and amount > 0 and price > 0):
                return "There was an error in data input."
            
        table = []
        for name, details in self.items.items():
            total = details["amount"] * details["price"]
            table.append([name, details["amount"], details["price"], total])

        rendered_table = tabulate(
            table, 
            headers=["Item Name", "Amount", "Price/Item", "Total Price"], 
            tablefmt="grid"
        )
        return f"The order is correct. Here are the details:\n{rendered_table}"
                
    def total_price(self):
        total = 0
        for details in self.items.values():
            subtotal = details["amount"] * details["price"]
            total += subtotal
            
        if 200_000 < total <= 300_000:
            discount = 0.05
        elif 300_000 < total <= 500_000:
            discount = 0.08
        elif total > 500_000:
            discount = 0.10
        else:
            discount = 0.0
            
        final_price = int(total * (1 - discount))
        return f"Total price: {total}, Discount: {int(discount*100)}%, Final price: {final_price}"