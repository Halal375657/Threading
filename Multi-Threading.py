'''
    ধরি আমাদের কাস্টমার ৫ জন এবং ওয়েটার ১ জন যিনি অর্ডার নেয়, রান্না করে ও খাবার রেডি করার কাজ একাই করে থাকেন

ওয়েটার কে ধরি সিপিইউ এর একটা থ্রেড, একটা থ্রেড একই সময়ে মাত্র একটা কাজ সম্পন্ন করতে পারে।.
'''
# Multi-Theading Programming.

import time
import threading

def get_food(c_id):
    print("Customer %s's food is cooking.... "%c_id)
    time.sleep(5)
    print("Customer %s's food is ready "%c_id)
    print("======Ending time: " + str(time.ctime()))

def make_order(c_id):
    print("Running Thread: " + str(threading.current_thread().name))
    print("Customer %s's food is Ordering.... "%c_id)
    get_food(c_id)


if __name__ == "__main__":

    cust = 5
    threads = []

    print("======Starting time: " + str(time.ctime()))

    for c in range(cust):
        thread = threading.Thread(target=make_order, args=(c,))
        thread.start()


    for t in threads:
        t.join()
