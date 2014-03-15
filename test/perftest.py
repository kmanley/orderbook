import os
import time
import random
import sys
sys.path.append(os.path.abspath(".."))
from orderbook import OrderBook

"""
Sample results on Lenovo X200 laptop, Linux Mint 14
processor	: 1
vendor_id	: GenuineIntel
cpu family	: 6
model		: 23
model name	: Intel(R) Core(TM)2 Duo CPU     P8400  @ 2.26GHz
stepping	: 6
microcode	: 0x60c
cpu MHz		: 800.000
cache size	: 3072 KB

maxprice     trading range       orders/sec
50000            1%                67,500
50000            2%                49,750
50000            3%                40,100
50000            4%                34,600
50000            5%                28,900
50000           10%                17,000
50000           15%                12,000
50000           20%                 8,700
50000           25%                 7,500
50000           50%                 4,000
"""

def perftest():
    class MyOrderBook(OrderBook):
        trades = 0
        def execute(self, trader_buy, trader_sell, price, size):
            MyOrderBook.trades += 1
    
    import time, random
    ITERS = 100000
    max_price = 50000
    min_random_price = int(max_price * .25)
    max_random_price = int(max_price * .75)
    print "max price: %d" % max_price
    print "random trading range: %d-%d (%.2f%%)" % (min_random_price, max_random_price, (max_random_price-min_random_price)/float(max_price)*100)
    ob = MyOrderBook("FOOBAR", max_price=max_price)
    elapsed = 0.0
    for i in range(ITERS):
        buysell, qty, price, trader = random.choice([0,1]), random.randrange(1,1000), \
                random.randrange(min_random_price, max_random_price), 'trader %s' % random.randrange(1000)
        start = time.clock()
        ob.limit_order(buysell, qty, price, trader)
        elapsed += (time.clock() - start)
    elapsed = elapsed * 1000.
        
    print "# orders: %d" % ITERS
    print "elapsed: %.2f msecs" % elapsed
    print "# trades: %d" % MyOrderBook.trades
    print "%.2f orders/sec" % (ITERS/elapsed*1000.)
    print "check memory use for pid %s" % os.getpid()
    print "press Enter to quit"
    raw_input()

if __name__ == "__main__":
    perftest()