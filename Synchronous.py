# Resturant management.
# Suppose, our customer is 5 and the waiter is the one who takes orders, cooks and prepares food.
# Suppose, Waiter is a thread of CPU.A thread can done at a time only one task.

# Note: Python is a Single Threaded programming language.


import time

class Synchronous(object):
    def get_food(self, cust_id):
        print("Customer %s's food is cooking....."%(cust_id))
        time.sleep(5)
        print("Customer %s's food is ready"%(cust_id))

    def make_order(self, cust_id):
        print("Customer %s's food is Ordering....."%(cust_id))
        self.get_food(cust_id)


if __name__ == "__main__":

    syns = Synchronous()
    customer = 5
    print("====Starting time: " + str(time.ctime()))

    for cust in range(customer):
        syns.make_order(cust)

    print("====Ending time: " + str(time.ctime()))
        
