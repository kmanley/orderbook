import os
import time
import random
import sys
sys.path.append(os.path.abspath(".."))
from orderbook import OrderBook

def orderbook_demo():
    import time, random
    ITERS = 100000
    max_price = 10
    ob = OrderBook("FOOBAR", max_price=max_price)
    start = time.clock()
    for i in range(ITERS):
        os.system("clear")
        buysell, qty, price, trader = random.choice([0,1]), random.randrange(1,50), \
                random.randrange(1,max_price), 'trader %s' % random.randrange(1000)
        print "NEW ORDER: %s %s %s @ %s" % (trader, "BUY" if buysell==0 else "SELL", qty, price)
        ob.limit_order(buysell, qty, price, trader)
        print ob.render()
        raw_input()

if __name__ == "__main__":
    orderbook_demo()