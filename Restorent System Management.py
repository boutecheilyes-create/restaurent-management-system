class MenueItem:
    menue_item_id = 1
    def __init__(self, name, price, category, is_available):
        self.menue_item_id = MenueItem.menue_item_id
        self.name = name
        self.price = price
        self.category = category
        self.is_available = is_available
        MenueItem.menue_item_id += 1
    def item_info(self):
        print(f"menue_item_id : {self.menue_item_id}")
        print(f"name : {self.name}")
        print(f"price : {self.price}")
        print(f"category : {self.category}")
        print(f"is_available : {self.is_available}")
class Customer:
    customer_id = 1
    def __init__(self, phone):
        self.customer_id = Customer.customer_id
        self.phone = phone
        self.orders = []
        Customer.customer_id += 1
    def customer_info(self):
        print(f"customer_id : {self.customer_id}")
        print(f"phoone : {self.phone}")
class OrderItem:
    def __init__(self, menue_item, quantity):
        self.menue_item = menue_item
        self.quantity = quantity
        self.subtoral = 0
    def update_quantity(self, q):
        self.quantity = q
    def order_item_info(self):
        print(f"quantity : {self.quantity}")
        print(f"subtoral : {self.subtoral}")
class Order:
    order_id = 1
    def __init__(self, customer, status):
        self.order_id = Order.order_id
        self.customer = customer
        self.items = []
        self.status = status
        self.total_price = 0
        Order.order_id += 1
class Table:
    table_id = 1
    def __init__(self, capacity, is_available):
        self.table_id = Table.table_id
        self.capacity = capacity
        self.is_available = is_available
        Table.table_id += 1
    def table_info(self):
        print(f"table_id : {self.table_id}")
        print(f"capacity : {self.capacity}")
        print(f"is_available : {self.is_available}")
    def chek_avaibility(self):
        return self.is_available

class Restorent:
    def __init__(self):
        self.menue_items = []
        self.order_items = []
        self.customers = []
        self.orders = []
        self.table = []
    def add_customer(self):
        is_running1 = True
        while is_running1:
            phone = input("Enter the phone number :")
            if len(phone) == 11 or len(phone) == 10:
                if phone.startswith("0"):
                    c = Customer(phone=phone)
                    self.customers.append(c)
                    print("Done")
                    is_running1 = False
                else:
                    print("phone number must start with 0")
            else:
                print("phone number must contains 10 or 11 numbers")
    def create_order(self):
        c_id = int(input("Enter the customer id :"))
        for c in self.customers:
            if c.customer_id == c_id:
                orde = OrderItem(customer=c, status="")
                print("Done")
        else:
            print(f"No customer with id {c_id}, please try again !")
    def create_menue_item(self):
        name = input("Enter the name :")
        price = float(input("Enter the price :"))
        category = input("Enter the category :")
        m_i = MenueItem(name, price, category, is_available=True)
        self.menue_items.append(m_i)
        print("Done")
    def create_OrderItem(self):
            menue_item = int(input("Enter the menue item id :"))
            for i in self.menue_items:
                if i.menue_item_id == menue_item:
                    quantity = int(input("Enter the quantity :"))
                    o_id = int(input("Enter the order id :"))
                    for o in self.orders:
                        if o.order_id == o_id:
                            oi = OrderItem(i, quantity)
                            sub = oi.quantity * oi.i.price
                            oi.subtoral = sub
                            o.total_price += sub
                            o.items.append(oi)
                            self.order_items.append(oi)
                            print("Done")
            else:
                print(f"No menue_item with id {menue_item}, please try again !")

    def show_orders(self):
        if self.orders:
            for s in self.orders:
                        print(f"order_id : {s.order_id}")
                        print(f"customer_id : {s.customer.customer_id}")
                        print(f"status : {s.status}")
                        print(f"total_price : {s.total_price}")
                        print("----------")
        else:
            print("print theire is no orders yet !")
    def search_order(self):
        id = int(input("Enter the order id :"))
        for o in self.orders:
            if o.order_id == id:
                        print(f"order_id : {o.order_id}")
                        print(f"customer_id : {o.customer.customer_id}")
                        print(f"status : {o.status}")
                        print(f"total_price : {o.total_price}")
                        break
        else:
            print("order was not found !")
    def show_customers(self):
        if self.customers:
            for s in self.customers:
                s.customer_info()
        else:
            print("theire is no customers yet !")
    def search_customer(self):
        id1 = int(input("Enter the order id :"))
        for o in self.customers:
            if o.order_id == id1:
                        o.customer_info()
                        for s in self.orders:
                            if s.customer.customer_id == id1:
                                print(f"order_id : {id1}")
                                break
                        else:
                            print("this customer has no order !")
                            break
        else:
            print("order was not found !")
    def searh_orderitem(self):
        id = int(input("Enter the order_item id :"))
        for oi in self.order_items:
            if oi.menue_item.menue_item_id == id:
                oi.order_item_info()
                break
        else:
            print(f"order item was not found !")
    def show_searh_orderitems(self):
        if self.order_items:
            for oi in self.order_items:
                oi.order_item_info()
                print("----------")
        else:
            print("No order items yet !")
    def add_order_item(self):
        id1 = int(input("Enter the order_item id :"))
        id2 = int(input("Enter the order id :"))
        for o in self.orders:
            if o.order_id == id2 :
                for oi in self.order_items:
                    if id1 == oi.menue_item.menue_item_id:
                        o.items.append(oi)
                        o.total_price += oi.subtoral
                        print("Done")
                        break
                else:
                    print("order_item was not found !")
                    break
        else:
            print("oder was not found !")
    def calculate_restorent_revenue(self):
        tot = 0
        for o in self.orders:
            tot += o.total_price
        return tot
    def update_quantity(self):
        id4 = int(input("Ente the order_item id :"))
        q = int(input("Enter the new quantity :"))
        for oi in self.order_items:
            oi.update_quantity(q)
            oi.subtoral = oi.quantity * oi.menue_item.price
            print("Done")
            break
        else:
            print("order_item was not found !")

while True:
    print("1. add_customer")
    
r = Restorent()



                



                 


    



            

        















        