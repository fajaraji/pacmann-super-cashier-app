# import library
from tabulate import tabulate

# create class
class Transaction:
    def __init__(self):
        self.items = {} # {"name": {"amount": int, "price": float}}

    def add_item(self, name: str, amount: int, price: float):
        self.items[name] = {"amount": amount, "price": price}
        return f"Item {name} added successfully."
    
    def update_item_name(self, old_name: str, new_name: str):
        if old_name in self.items:
            self.items[new_name] = self.items.pop(old_name)
            return f"Item name updated from {old_name} to {new_name}."
        return f"Item {old_name} not found."
    
    def update_item_amount(self, name: str, new_amount: int):
        if name in self.items:
            self.items[name]["amount"] = new_amount
            return f"Item {name} amount updated to {new_amount}."
        return f"Item {name} not found."
    
    def update_item_price(self, name: str, new_price: float):
        if name in self.items:
            self.items[name]["price"] = new_price
            return f"Item {name} price updated to {new_price}."
        return f"Item {name} not found."
    
    def delete_item(self, name: str):
        if name in self.items:
            del self.items[name]
            return f"Item {name} deleted successfully."
        return f"Item {name} not found."
    
    def reset_transaction(self):
        self.items.clear()
        return "Transaction reset successfully."
    
    def check_order(self):
        if not self.items:
            return "No items in the transaction."
        
        if name and amount > 0 and price > 0:
            table = []
            for name, details in self.items.items():
                table.append([name, details["amount"], details["price"], details["amount"] * details["price"]])
            print("The order is correct")
            return tabulate(table, headers=["Item Name", "Amount", "Price/Item", "Total Price"], tablefmt="grid")
        else:
            return "There was an error in data input."

    def total_price(self):
        final_price = 0
        for details in self.items.values():
            subtotal = details["amount"] * details["price"]
            total += subtotal
            
            if 200_000 < total <= 300_000:
                discount = 0.05
                final_price = total * (1 - discount)
                return f"Total price: {total}, Discount: 5%, Final price: {final_price}"
            elif 300_000 < total <= 500_000:
                discount = 0.08
                final_price = total * (1 - discount)
                return f"Total price: {total}, Discount: 8%, Final price: {final_price}"
            elif total > 500_000:
                discount = 0.10
                final_price = total * (1 - discount)
                return f"Total price: {total}, Discount: 10%, Final price: {final_price}"
            else:
                final_price = total
                return f"Total price: {total}, No discount applied, Final price: {final_price}"
        
        
        