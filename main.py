# %% import class
from transaction import Transaction

# %% test case 1: customer wants to add 2 new items using add_item method
trx1 = Transaction()
print(trx1.add_item("Fried Chicken", 2, 20000))
print(trx1.add_item("Toothpaste", 3, 15000))
# %% test case 2: customer wants to delete toothpaste from the transaction using delete_item method
print(trx1.delete_item("Toothpaste"))

# %% test case 3: calculate final price, before final price showed, display order details using check_order method
print(trx1.check_order())
print(trx1.total_price())
# %% test case 4: customer wants to reset the transaction using reset_transaction method
print(trx1.reset_transaction())
    
# %% test case 5: another customer wants to add 3 new items using add_item method
trx2 = Transaction()
print(trx2.add_item("Rice", 5, 15000))
print(trx2.add_item("Eggs", 24, 2000))
print(trx2.add_item("Cooking Oil", 1, 25000))
# %% test case 6: customer wants to update Eggs amount from 12 to 18 using update_item_amount method
print(trx2.update_item_amount("Eggs", 72))

# %% test case 7: customer wants to calculate final price, before final price showed, display order details using check_order method
print(trx2.check_order())
print(trx2.total_price())
