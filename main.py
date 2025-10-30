# import class
from transaction import Transaction

# test case 1: customer wants to add 2 new items using add_item method
trx1 = Transaction()
print(trx1.add_item("Fried Chicken", 2, 20000))
print(trx1.add_item("Toothpaste", 3, 15000))

# test case 2: customer wants to delete Toothpaste from the transaction using delete_item method
print(trx1.delete_item("Toothpaste"))

# test case 3: customer wants to reset the transaction using reset_transaction method
print(trx1.reset_transaction())

# test case 4: calculate final price, before final price showed, display order details using check_order method
print(trx1.check_order())
print(trx1.total_price())


    