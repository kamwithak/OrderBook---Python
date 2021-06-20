class Order(object):
    def __init__(self, side, price, size, timestamp=None, order_id=None):
        self.side = side
        self.price = price
        self.size = size
        self.timestamp = timestamp
        self.order_id = order_id

    def __repr__(self):
        return '{0} {1} units at {2}'.format(self.side, self.size, self.price)